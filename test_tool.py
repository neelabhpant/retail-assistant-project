# test_tool.py
from tools.order_history_tool import OrderHistoryTool
from tools.return_item_tool import ReturnItemTool

def run_tests():
    print("--- Running Tool Tests ---")
    
    # === Test OrderHistoryTool ===
    print("\n--- Testing OrderHistoryTool ---")
    order_history_tool = OrderHistoryTool()
    
    # Test Case 1: Valid customer
    print("\n[Test Case 1.1: Valid Customer 'C001']")
    result = order_history_tool.run(customer_id='C001')
    print("Result:\n" + result)

    # Test Case 2: Invalid customer
    print("\n[Test Case 1.2: Invalid Customer 'C999']")
    result = order_history_tool.run(customer_id='C999')
    print("Result:\n" + result)
    
    # === Test ReturnItemTool ===
    print("\n--- Testing ReturnItemTool ---")
    return_item_tool = ReturnItemTool()

    # Test Case 1: Eligible for return
    print("\n[Test Case 2.1: Eligible Return (Delivered Order)]")
    result = return_item_tool.run(customer_id='C001', order_id='12345', product_sku='LP123')
    print("Result:\n" + result)

    # Test Case 2: Not eligible for return
    print("\n[Test Case 2.2: Ineligible Return (Shipped Order)]")
    result = return_item_tool.run(customer_id='C001', order_id='12346', product_sku='NCH789')
    print("Result:\n" + result)

    # Test Case 3: Item not in order
    print("\n[Test Case 2.3: Item Not Found in Order]")
    result = return_item_tool.run(customer_id='C001', order_id='12345', product_sku='XYZ999')
    print("Result:\n" + result)

    print("\n--- All Tests Complete ---")

if __name__ == "__main__":
    run_tests()