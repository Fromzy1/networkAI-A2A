from agents.planner_agent import PlannerAgent
from agents.elastic_agent import ElasticAgent
from agents.viz_agent import VizAgent
from messaging.message import create_message

planner = PlannerAgent("PlannerAgent")
elastic = ElasticAgent("ElasticAgent")
viz = VizAgent("VizAgent")

user_query = input("Ask your question: ")
msg = create_message("User", "PlannerAgent", {"query": user_query})

# A2A chain
response1 = planner.receive(msg)
response2 = elastic.receive(response1)
response3 = viz.receive(response2)