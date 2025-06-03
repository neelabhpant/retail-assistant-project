# test_tool.py
from tools.order_history_tool import OrderHistoryTool
from tools.return_item_tool import ReturnItemTool
from tools.faq_tool import FAQTool
from tools.product_search_tool import ProductSearchTool

def run_tests():
    print("--- Running All Tool Tests ---")
    
    # === Test OrderHistoryTool ===
    print("\n--- Testing OrderHistoryTool ---")
    order_history_tool = OrderHistoryTool()
    print("[Test Case 1.1: Valid Customer 'C001']")
    result = order_history_tool.run(customer_id='C001')
    print("Result:\n" + result)
    
    # === Test ReturnItemTool ===
    print("\n--- Testing ReturnItemTool ---")
    return_item_tool = ReturnItemTool()
    print("\n[Test Case 2.1: Eligible Return (Delivered Order)]")
    result = return_item_tool.run(customer_id='C001', order_id='12345', product_sku='LP123')
    print("Result:\n" + result)
    
    # === Test FAQTool ===
    print("\n--- Testing FAQTool ---")
    try:
        faq_tool = FAQTool()
        print("\n[Test Case 3.1: Query about returns]")
        result = faq_tool.run(query="how do I return something?")
        print("Result:\n" + result)
    except Exception as e:
        print(f"Could not run FAQTool test: {e}")

    # === Test ProductSearchTool ===
    print("\n--- Testing ProductSearchTool ---")
    try:
        product_search_tool = ProductSearchTool()
        print("\n[Test Case 4.1: Query for a computer]")
        # Test with a semantic query
        result = product_search_tool.run(query="a computer for work")
        print("Result:\n" + result)
    except Exception as e:
        print(f"Could not run ProductSearchTool test: {e}")

    print("\n--- All Tests Complete ---")

if __name__ == "__main__":
    run_tests()