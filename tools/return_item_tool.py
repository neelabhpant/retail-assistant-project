# tools/return_item_tool.py
import json
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from config.config import settings

def _load_orders_data():
    """A helper function to load orders data from the JSON file."""
    with open(settings.orders_data_path, 'r') as f:
        return json.load(f)

class ReturnItemInput(BaseModel):
    """Input for the ReturnItemTool."""
    customer_id: str = Field(description="The customer's unique identifier.")
    order_id: str = Field(description="The unique identifier of the order.")
    product_sku: str = Field(description="The unique SKU of the product to be returned.")

class ReturnItemTool(BaseTool):
    name: str = "Return Item Tool"
    description: str = "Processes a return request for a specific item from a customer's order."
    args_schema: Type[BaseModel] = ReturnItemInput

    def _run(self, customer_id: str, order_id: str, product_sku: str) -> str:
        orders_data = _load_orders_data()

        # Find the customer
        customer_data = next((c for c in orders_data if c["customer_id"] == customer_id), None)
        if not customer_data:
            return f"Error: Customer with ID '{customer_id}' not found."

        # Find the order
        order_data = next((o for o in customer_data["orders"] if o["order_id"] == order_id), None)
        if not order_data:
            return f"Error: Order with ID '{order_id}' not found for customer {customer_id}."

        # Find the item in the order
        item_data = next((i for i in order_data["items"] if i["sku"] == product_sku), None)
        if not item_data:
            return f"Error: Item with SKU '{product_sku}' not found in order {order_id}."
        
        item_name = item_data['name']

        # Check return eligibility based on order status
        if order_data["status"] == "Delivered":
            return f"Return approved for item: '{item_name}' (SKU: {product_sku}) from order {order_id}. Please follow the instructions sent to your email."
        else:
            return f"Return denied for item: '{item_name}' (SKU: {product_sku}). Reason: The order status is '{order_data['status']}', not 'Delivered'."