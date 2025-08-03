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
        payment_val_object = json.loads(msg.get_body())
        payment_id = payment_val_object.get("payment_id")
        order_id = payment_val_object.get("order_id")
        invoice_amount = payment_val_object.get("invoice_amount")
        payment_status = payment_val_object.get("payment_status")

        #generate invoice
        if payment_status == "Success":
            invoice_num = "inv_"+str(uuid.uuid4())
      
        client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
        db = client.get_database_client(COSMOS_DB_NAME)
        orders_container = db.get_container_client("orders")
        inv_container = db.get_container_client("inventory_master")

        # update orders container insert invoice num
        get_order_id_query = "SELECT * FROM c where c.order_id = @order_id"
        get_order_id_params = [{"name": "@order_id", "value": order_id}]
        order_item = list(orders_container.query_items(
            query=get_order_id_query,
            parameters=get_order_id_params,
            enable_cross_partition_query=True
        ))
 
        updated_order_object = order_item[0]
        product_id = updated_order_object.get("product_id")
        order_qty = updated_order_object.get("order_qty")
        updated_order_object["invoice_status"] = invoice_num
        updated_order_object["shipment_status"] = "Invoice generated. Preparing for dispatch"
        orders_container.replace_item(item=updated_order_object, body=updated_order_object)
        print("Updated orders")

        # update inventory
        get_inv_query = "SELECT * FROM c where c.product_id = @product_id"
        get_inv_query_params = [{"name": "@product_id", "value": product_id}]
        inv_item = list(inv_container.query_items(
            query=get_inv_query,
            parameters=get_inv_query_params,
            enable_cross_partition_query=True
        ))

        updated_inv_object = inv_item[0]
        stock_qty = updated_inv_object.get("stock_qty")
        if stock_qty > order_qty:
            updated_inv_object["stock_qty"] = stock_qty - order_qty
            inv_container.replace_item(item=updated_inv_object, body=updated_inv_object)
            print("Updated inventory")
        else:
            logging.error("Not enough Inventory")

        # send msg to service bus
        queue_name = "dispatch"
        with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
            sender = client.get_queue_sender(queue_name=queue_name)
            with sender:
                dispatch_object = {
                    "invoice_no" : invoice_num,
                    "invoice_amount" : invoice_amount,
                    "order_id" : order_id
                }
                message = ServiceBusMessage(json.dumps(dispatch_object))
                sender.send_messages(message)
                logging.info("Message sent to Service Bus.")
    
    except Exception as e:
        logging.error('Msg failed to deliver to dispatch queue',e)