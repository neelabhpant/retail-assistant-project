# crew/tasks.py
from crewai import Task

class RetailTasks:
    def route_query_task(self, agent, query: str) -> Task:
        return Task(
            description=f"Analyze the user's query: '{query}'.\n"
                        "Identify the main intents (e.g., order lookup, return request, product question, faq) "
                        "and pass the necessary information to the appropriate agent.",
            expected_output="A clear and concise summary of the user's intents and the information required to address them. "
                            "For example: 'The user C001 wants to see their order history and also wants to return an item.'",
            agent=agent,
        )

    def retail_inquiry_task(self, agent) -> Task:
        return Task(
            description="Based on the routed query, use your available tools to find the necessary information. "
                        "Handle inquiries about order history, process returns, search for products, or find answers in the FAQ.",
            expected_output="The specific information retrieved from the tools. This could be order details, "
                            "a return confirmation, a list of products, or an answer from the FAQs. "
                            "Provide a factual, direct output from the tool.",
            agent=agent,
        )

    def summarize_response_task(self, agent) -> Task:
        return Task(
            description="Review the entire conversation, including the user's original query and the results from the "
                        "Retail Assistant Agent. Synthesize this information into a single, cohesive, and friendly response. "
                        "Address all parts of the user's query in your final answer.",
            expected_output="A final, well-formatted, and conversational response to the user that includes all the "
                            "information they requested. For example: 'Hi! Here is your order history... Regarding your return, "
                            "it has been approved... I also found some products you might like...'",
            agent=agent,
        )