import azure.functions as func
import logging, uuid, json, os
from azure.servicebus import ServiceBusMessage, ServiceBusClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing submit_order request.')
    print('Processing submit_order request.')

    try:
        order_data = req.get_json()
    except Exception as e:
        logging.error(f"Invalid JSON: {e}")
        print(e)
        return func.HttpResponse("Invalid JSON", status_code=400)

    order_id = str(uuid.uuid4())
    order_data['order_id'] = order_id

    try:
        SERVICE_BUS_CONNECTION_STRING = os.environ["SERVICE_BUS_CONNECTION_STRING"]
        queue_name = "orders"

        with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
            sender = client.get_queue_sender(queue_name=queue_name)
            with sender:
                message = ServiceBusMessage(json.dumps(order_data))
                sender.send_messages(message)
                logging.info("Message sent to Service Bus.")
        return func.HttpResponse(f"Order placed. Order ID: {order_id}", status_code=200)

    except Exception as e:
        logging.error(f"Error occurred while sending message: {e}")
        print(e)
        return func.HttpResponse(f"Order failed {e}", status_code=500)
