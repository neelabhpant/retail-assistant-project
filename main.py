# main.py
from crew.crew_setup import RetailCrew

def main():
    print("--- Retail Assistant Crew ---")
    
    query = """
    I am customer C001. I would like to see my most recent order history. 
    Also, can you tell me what your return policy is? 
    Finally, I'm looking for a good pointing device for my new computer.
    """
    
    print(f"\nCustomer Query:\n{query}")
    
    retail_crew = RetailCrew(query)
    
    print("\n--- Kicking off the crew... ---")
    result = retail_crew.run()
    
    print("\n--- Crew execution complete! ---")
    print("\nFinal Result:")
    print(result)

if __name__ == "__main__":
    main()