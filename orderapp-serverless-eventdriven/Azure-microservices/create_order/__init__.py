import logging
import azure.functions as func
import json, os,uuid
from azure.cosmos import CosmosClient, exceptions
from azure.servicebus import ServiceBusMessage, ServiceBusClient


COSMOS_ENDPOINT = os.environ["COSMOS_ENDPOINT"]
COSMOS_KEY = os.environ["COSMOS_KEY"]
COSMOS_DB_NAME = "projectdb"
COSMOS_CONTAINER_NAME = "orders"
PAYMENT_QUEUE_NAME = "payment"
SERVICE_BUS_CONNECTION_STRING = os.environ["SERVICE_BUS_CONNECTION_STRING"]

def main(msg: func.ServiceBusMessage):
    logging.info("ServiceBus queue trigger function processed a message.")

    try:
        #load to cosmos
        order_data = json.loads(msg.get_body())
        
        order_object = {
            "id" : str(uuid.uuid4()),
            "order_id" : order_data.get("order_id"),
            "customer_id" : order_data.get("customer_id"),
            "product_id" : order_data.get("product_id"),
            "order_qty" : order_data.get("order_qty"),
            "payment_amount": order_data.get("payment_amount"),
            "payment_status" : "pending",
            "shipment_status" : "pending",
            "invoice_status" : "pending",
            "email_id" : order_data.get("email_id"),
            "notification" : "pending",
            "raw_input" : order_data,
            "order_timestamp" : order_data.get("order_timestamp")
        } 

        client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
        db = client.get_database_client(COSMOS_DB_NAME)
        container = db.get_container_client(COSMOS_CONTAINER_NAME)
        container.create_item(body=order_object)

    except Exception as e:
        logging.error(f'Failed to create order {order_data["order_id"]}')

    try:
        with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
            sender = client.get_queue_sender(queue_name=PAYMENT_QUEUE_NAME)

            with sender:
                payment_msg = {
                "order_id" : order_data.get("order_id"),
                "order_qty" : order_data.get("order_qty"),
                "product_id" : order_data.get("product_id"),
                "payment_amount" : order_data.get("payment_amount")
                }

                message = ServiceBusMessage(json.dumps(payment_msg))
                sender.send_messages(message)
                logging.info("Message sent to Service Bus.")

    except Exception as e:
        logging.error(f'Failed to send payment message for {order_data["order_id"]}')
