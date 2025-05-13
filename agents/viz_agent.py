from messaging.base_agent import BaseAgent
from messaging.message import create_message
import chart_util

class VizAgent(BaseAgent):
    def receive(self, message):
        print(f"[VizAgent] Received data to visualize")
        data = message["content"]["results"]
        chart = chart_util.ChartUtil()
        chart.generate_chart(data)
        return create_message(self.agent_id, "User", {"status": "Chart displayed"})