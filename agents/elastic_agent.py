from messaging.base_agent import BaseAgent
from messaging.message import create_message
import ElasticTools

class ElasticAgent(BaseAgent):
    def __init__(self, agent_id):
        super().__init__(agent_id)
        self.et = ElasticTools.Tools()
        self.index_dict = self.et.get_indices_dict()

    def receive(self, message):
        print(f"[ElasticAgent] Executing query for: {message['content']}")
        index = message['content']['index']
        query = message['content']['natural_language']
        
        # Assume we still need LLM to translate query
        # LLM uses prompt_1.txt dynamically injected with schema
        schema = self.et.get_index_schema(self.index_dict[index])
        prompt = open("prompt_1.txt").read().format(schema=schema)
        
        from OpenAIClient import Client
        LLM = Client()
        es_query = LLM.generate_non_streaming_response(query, system_prompt=prompt)
        
        # Execute query
        search_results = self.et.search_results(self.index_dict[index], es_query=json.loads(es_query))
        return create_message(self.agent_id, "VizAgent", {"results": search_results})