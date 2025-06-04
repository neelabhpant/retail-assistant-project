# crew/crew_setup.py
from crewai import Crew, Process
from crew.agents import RetailAgents
from crew.tasks import RetailTasks

agents = RetailAgents()
tasks = RetailTasks()

query_router = agents.query_router_agent()
retail_assistant = agents.retail_assistant_agent()
summarizer = agents.summarizer_agent()

class RetailCrew:
    def __init__(self, query: str):
        self.query = query

    def run(self):
        route_query = tasks.route_query_task(query_router, self.query)
        inquiry = tasks.retail_inquiry_task(retail_assistant)
        summary = tasks.summarize_response_task(summarizer)

        crew = Crew(
            agents=[query_router, retail_assistant, summarizer],
            tasks=[route_query, inquiry, summary],
            process=Process.sequential,
            verbose=True  # verbose=2
        )

        result = crew.kickoff()
        return result