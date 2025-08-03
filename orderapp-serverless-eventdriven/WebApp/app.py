from flask import Flask, render_template, request, jsonify
from azure.cosmos import CosmosClient
import os, uuid, requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "projectdb"
PRODUCTS_CONTAINER = "product_master"

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
db = client.get_database_client(DATABASE_NAME)
product_container = db.get_container_client(PRODUCTS_CONTAINER)
customer_container = db.get_container_client("customer_master")

def create_customer(customer_name, email_id, location):
    get_customer = "SELECT * FROM c where c.customer_email = @customer_email"
    params = [{"name": "@customer_email", "value": email_id}]
    cust_item = list(customer_container.query_items(
        query=get_customer,
        parameters=params,
        enable_cross_partition_query=True
    ))

    if cust_item:
        cust_obj = cust_item[0]
        reg_msg = "You are already registered"
    else:
        cust_info = {
            "id" : str(uuid.uuid4()),
            "customer_id" : customer_name,
            "customer_name" : customer_name,
            "customer_email" : email_id,
            "location" : location
        }

        customer_container.create_item(cust_info)
        reg_msg = f"✅ Registered: {customer_name}, {email_id}, {location}"
    
    return reg_msg
  
@app.route("/")
def index():
    return render_template("landing.html")

@app.route('/register.html')
def register_page():
    return render_template('register.html')

@app.route('/shopping')
def shopping_page():
    products = list(product_container.read_all_items())
    return render_template("shopping.html", products=products)

@app.route('/register_customer', methods=['POST'])
def register_customer():
    data = request.get_json()
    print(data)
    customer_name = data.get("customer_name")
    email_id = data.get("email_id")
    location = data.get("location")

    if not all([customer_name, email_id, location]):
        return jsonify({ "success": False, "message": "All fields are required." }), 400
    reg_msg = create_customer(customer_name, email_id, location)
    return jsonify({ "success": True, "message": reg_msg })

@app.route("/submit_order", methods=["POST"])
def submit_order():
    data = request.get_json()
    customer_id = data.get("customer_id")
    email_id = data.get("email_id")
    payment_amount = int(data.get("payment_amount"))
    product_id = data.get("product_id")
    cart = data.get("cart", [])

    get_customer = "SELECT * FROM c where c.customer_email = @customer_email"
    params = [{"name": "@customer_email", "value": email_id}]
    cust_item = list(customer_container.query_items(
        query=get_customer,
        parameters=params,
        enable_cross_partition_query=True
    ))

    # If customer exists
    if cust_item: 
        payload = {
            "customer_id": customer_id,
            "email_id": email_id,
            "product_id": cart[0].get("id"),
            "order_qty": int(cart[0].get("qty")),
            "payment_amount": payment_amount
        }

        url = "https://testfuncapp001001.azurewebsites.net/api/submit_order"

        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        message = f"✅Thank you, your order has been placed. You will receive a msg shortly"
    else:
        message = f"❌Please register first"
    
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
