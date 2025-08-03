import logging
import azure.functions as func
import json, os,uuid
from azure.cosmos import CosmosClient, exceptions
from azure.servicebus import ServiceBusMessage, ServiceBusClient
from datetime import date, timedelta

COSMOS_ENDPOINT = os.environ["COSMOS_ENDPOINT"]
COSMOS_KEY = os.environ["COSMOS_KEY"]
COSMOS_DB_NAME = "projectdb"
SERVICE_BUS_CONNECTION_STRING = os.environ["SERVICE_BUS_CONNECTION_STRING"]

def main(msg: func.ServiceBusMessage):
    logging.info("ServiceBus queue trigger function processed a message.")

    try:
        msg = json.loads(msg.get_body())
        invoice_num = msg.get("invoice_no")
        order_id = msg.get("order_id")

        shipment_obj = {
            "id" : str(uuid.uuid4()),
            "order_id" : order_id,
            "delivery_partner" : "DHL",
            "AWB" : "AWB"+str(uuid.uuid4()),
            "shipment_date" : str(date.today()),
            "status" : "In transit",
            "expected_delivery_date" : str(date.today() + timedelta(days=2))
        }

        # cosmos 
        client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
        db = client.get_database_client(COSMOS_DB_NAME)
        orders_container = db.get_container_client("orders")
        ship_container = db.get_container_client("shipment")

        # insert shipment
        ship_container.create_item(body=shipment_obj)

        # update orders
        get_order_id_query = "SELECT * FROM c where c.order_id = @order_id"
        get_order_id_params = [{"name": "@order_id", "value": order_id}]
        order_item = list(orders_container.query_items(
            query=get_order_id_query,
            parameters=get_order_id_params,
            enable_cross_partition_query=True
        ))
 
        updated_order_object = order_item[0]
        email_id = updated_order_object.get("email_id")
        shipment_obj["email_id"] = email_id
        updated_order_object["shipment_status"] = f"Tracking no. {shipment_obj.get('AWB')}"
        updated_order_object["notification"] = "Sent to customer"
        orders_container.replace_item(item=updated_order_object, body=updated_order_object)
        print("Updated orders")

        # email service bus
        queue_name = "email_service"
        with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
            sender = client.get_queue_sender(queue_name=queue_name)
            with sender:
                message = ServiceBusMessage(json.dumps(shipment_obj))
                sender.send_messages(message)
                logging.info("Message sent to Service Bus.")

    except Exception as e:
        logging.error(e)