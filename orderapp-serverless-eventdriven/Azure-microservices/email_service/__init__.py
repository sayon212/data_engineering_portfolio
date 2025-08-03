import azure.functions as func
from azure.communication.email import EmailClient
import json, os

def main(msg: func.ServiceBusMessage):
    try:
        SENDER_ADDRESS = os.environ["SENDER_ADDRESS"]
        ACS_CONNECTION_STRING = os.environ["ACS_CONNECTION_STRING"]
        client = EmailClient.from_connection_string(ACS_CONNECTION_STRING)
        bus_msg = json.loads(msg.get_body())

        order_id = bus_msg.get("order_id")
        delivery_partner = bus_msg.get("delivery_partner")
        AWB = bus_msg.get("AWB")
        dispatch_date = bus_msg.get("shipment_date")
        expected_delivery_date = bus_msg.get("expected_delivery_date")
        to_mail = bus_msg.get("email_id")

        plain_text_msg = (
            f"Hello,\n\n"
            f"Your order {order_id} is confirmed and shipped through {delivery_partner} on {dispatch_date} "
            f"with tracking number {AWB}.\n"
            f"Expected delivery date: {expected_delivery_date}.\n\n"
            f"Thank you for shopping with us!"
        )

        message = {
            "senderAddress": SENDER_ADDRESS,
            "recipients": {
                "to": [{"address": to_mail}]
            },
            "content": {
                "subject": "Order Status",
                "plainText": plain_text_msg
            },
            
        }
        print(message)
        poller = client.begin_send(message)
        result = poller.result()
        print("Message sent: ", result)

    except Exception as ex:
        print(ex)