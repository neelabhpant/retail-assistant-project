# crew/agents.py
from crewai import Agent
from utils.llm_loader import llm
from tools.product_search_tool import ProductSearchTool
from tools.faq_tool import FAQTool
from tools.order_history_tool import OrderHistoryTool
from tools.return_item_tool import ReturnItemTool

class RetailAgents:
    def query_router_agent(self) -> Agent:
        return Agent(
            role="Query Router Agent",
            goal="Examine the user query and route it to the appropriate specialist agent. "
                 "The query might involve one or more topics like order status, returns, product questions, or general FAQs.",
            backstory="You are a master at understanding user intent. Your primary function is to analyze incoming "
                      "queries and decide which specialized agent is best equipped to handle the request. "
                      "You ensure that the query is directed efficiently to provide the user with the quickest "
                      "and most accurate response.",
            llm=llm,
            verbose=True,
            allow_delegation=True # Allows this agent to delegate to the Retail Assistant
        )

    def retail_assistant_agent(self) -> Agent:
        # Instantiate tools inside the method for robustness
        return Agent(
            role="Retail Assistant Agent",
            goal="Handle specific customer inquiries related to order history, returns, product searches, and FAQs "
                 "by using a dedicated set of tools.",
            backstory="You are a highly skilled customer service representative with expertise in retail operations. "
                      "You have access to a suite of tools that allow you to look up order details, process returns, "
                      "search the product catalog, and answer frequently asked questions. Your goal is to provide "
                      "accurate and helpful information for each specific task you are given.",
            llm=llm,
            verbose=True,
            tools=[
                OrderHistoryTool(),
                ReturnItemTool(),
                FAQTool(),
                ProductSearchTool(),
            ],
        )

    def summarizer_agent(self) -> Agent:
        return Agent(
            role="Summarizer Agent",
            goal="Synthesize the information gathered by other agents into a single, cohesive, and friendly response "
                 "to the user. Ensure the final answer is easy to understand and directly addresses all parts of the user's original query.",
            backstory="You are a communications expert. After the specialist agents have done their work, you take all "
                      "their findings and craft a final, polished response. You are skilled at making complex "
                      "information simple and presenting it in a warm, helpful, and conversational tone.",
            llm=llm,
            verbose=True,
        )