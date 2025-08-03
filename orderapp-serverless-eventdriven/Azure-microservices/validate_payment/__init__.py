import logging
import azure.functions as func
import json, os,uuid
from azure.cosmos import CosmosClient, exceptions
from azure.servicebus import ServiceBusMessage, ServiceBusClient


COSMOS_ENDPOINT = os.environ["COSMOS_ENDPOINT"]
COSMOS_KEY = os.environ["COSMOS_KEY"]
COSMOS_DB_NAME = "projectdb"
SERVICE_BUS_CONNECTION_STRING = os.environ["SERVICE_BUS_CONNECTION_STRING"]

def main(msg: func.ServiceBusMessage):
    logging.info("ServiceBus queue trigger function processed a message.")

    try:
        #load to cosmos
        payment_data = json.loads(msg.get_body())
        product_id = payment_data.get("product_id")
        order_qty = payment_data.get("order_qty")
        order_id = payment_data.get("order_id")
        payment_amount = payment_data.get("payment_amount")
        
        client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
        db = client.get_database_client(COSMOS_DB_NAME)
        product_container = db.get_container_client("product_master")
        orders_container = db.get_container_client("orders")
        payment_container = db.get_container_client("payments")

        # validate payment
        product_query = "SELECT c.price FROM c WHERE c.product_id = @product_id"
        parameters = [{"name": "@product_id", "value": product_id}]

        query_out = list(product_container.query_items(
            query=product_query,
            parameters=parameters,
            enable_cross_partition_query=True))

        unit_price = query_out[0]['price']
        total_price = order_qty * unit_price

        if payment_amount == total_price:
            payment_status = "Success"
            invoice_status = "In Progress"
        else:
            payment_status = "Failed"      
            invoice_status = "Rejected"


        # update orders container
        get_order_id_query = "SELECT * FROM c where c.order_id = @order_id"
        get_order_id_params = [{"name": "@order_id", "value": order_id}]
        order_item = list(orders_container.query_items(
            query=get_order_id_query,
            parameters=get_order_id_params,
            enable_cross_partition_query=True
        ))
        updated_order_object = order_item[0]
        email_id = updated_order_object["email_id"]
        updated_order_object["payment_status"] = payment_status
        updated_order_object["invoice_status"] = invoice_status
        orders_container.replace_item(item=updated_order_object, body=updated_order_object)
        print("Updated orders")

        # create new item in payment container
        payment_object = {
            "id" : str(uuid.uuid4()),
            "payment_id" : "pay_"+str(uuid.uuid4()),
            "order_id" : order_id,
            "payment_amount": payment_amount,
            "invoice_amount" : total_price,
            "payment_status" : payment_status
        }
        payment_container.create_item(body=payment_object)

        # send msg to invoice_inventory service bus if payment success
        if payment_status=="Success":
            queue_name = "invoice_inventory"
            with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
                sender = client.get_queue_sender(queue_name=queue_name)
                with sender:
                    message = ServiceBusMessage(json.dumps(payment_object))
                    sender.send_messages(message)
                    logging.info("Message sent to Service Bus.")
        else:
            queue_name = "email_service"
            failed_payment_object = {
                "to_mail" : email_id,
                "status" : "payment failure"
            }
            with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
                sender = client.get_queue_sender(queue_name=queue_name)
                with sender:
                    message = ServiceBusMessage(json.dumps(failed_payment_object))
                    sender.send_messages(message)
                    logging.info("Message sent to Service Bus.")

            
    except Exception as e:
        logging.error('Msg failed to deliver to inventory queue',e)
