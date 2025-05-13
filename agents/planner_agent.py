from messaging.base_agent import BaseAgent
from messaging.message import create_message

class PlannerAgent(BaseAgent):
    def receive(self, message):
        query = message['content']['query']
        print(f"[Planner] Received query: {query}")
        
        task = {
            "action": "search",
            "index": "kafka-application",
            "natural_language": query
        }
        return create_message(self.agent_id, "ElasticAgent", task)