# tools/order_history_tool.py
import json
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from config.config import settings

def _load_orders_data():
    """A helper function to load orders data from the JSON file."""
    with open(settings.orders_data_path, 'r') as f:
        return json.load(f)

class OrderHistoryInput(BaseModel):
    """Input model for the OrderHistoryTool, ensuring the customer_id is provided."""
    customer_id: str = Field(description="The unique identifier of the customer (e.g., C001).")

class OrderHistoryTool(BaseTool):
    name: str = "Order History Tool"
    description: str = "Looks up the complete order history for a given customer ID and returns a formatted string."
    args_schema: Type[BaseModel] = OrderHistoryInput

    def _run(self, customer_id: str) -> str:
        """The method that executes when the tool is called."""
        orders_data = _load_orders_data()
        customer_found = False
        for customer in orders_data:
            if customer["customer_id"] == customer_id:
                customer_found = True
                if customer["orders"]:
                    history_str = f"Order history for {customer['name']} (ID: {customer_id}):\n"
                    for order in customer['orders']:
                        history_str += f"- Order ID: {order['order_id']}, Date: {order['date']}, Status: {order['status']}\n"
                        for item in order['items']:
                            history_str += f"  - Item: {item['name']}, Price: ${item['price']}\n"
                    return history_str
                else:
                    return f"Customer {customer['name']} (ID: {customer_id}) has no orders."
    
        if not customer_found:
            return f"Error: Customer with ID '{customer_id}' not found."