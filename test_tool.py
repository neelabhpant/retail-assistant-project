# test_tool.py
from tools.order_history_tool import OrderHistoryTool

def run_tests():
    print("--- Running Tool Tests ---")
    
    # 1. Instantiate the class-based tool
    order_tool = OrderHistoryTool()
    
    # 2. Test Case: Valid customer with orders
    print("\n[Test Case 1: Valid Customer 'C001']")
    try:
        # Pass the argument directly by its name
        result_c001 = order_tool.run(customer_id='C001')
        print("Result:")
        print(result_c001)
    except Exception as e:
        print(f"An error occurred: {e}")

    # 3. Test Case: Invalid customer
    print("\n[Test Case 2: Invalid Customer 'C999']")
    try:
        # Pass the argument directly by its name
        result_c999 = order_tool.run(customer_id='C999')
        print("Result:")
        print(result_c999)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\n--- Tests Complete ---")

if __name__ == "__main__":
    run_tests()