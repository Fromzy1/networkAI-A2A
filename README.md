# ntsctAI-A2A

**Agent-to-Agent (A2A) AI System for Natural Language to Elasticsearch Querying and Visualization**

`ntsctAI-A2A` is an experimental modular AI system where multiple autonomous agents collaborate to answer natural language queries over Elasticsearch datasets. Inspired by multi-agent architectures and Model Context Protocol (MCP), each agent has a distinct role: planning, data retrieval, and visualization.

---

## 🧠 Key Concepts

- **PlannerAgent**: Interprets user questions and decomposes them into tasks.
- **ElasticAgent**: Generates and executes Elasticsearch queries using LLM + schema context.
- **VizAgent**: Visualizes structured results via graphs or tabular summaries.
- **Messaging Layer**: Standardized message format supports signatures (SACMP-ready).
- **MCP Compatibility**: Agents can be MCP-compliant tools or communicate in A2A mode.

---

## 📂 Project Structure

ntsctAI-a2a/
├── agents/
│   ├── planner_agent.py        # Understands intent and plans actions
│   ├── elastic_agent.py        # Generates and executes ES queries
│   └── viz_agent.py            # Handles visualization
│
├── messaging/
│   ├── base_agent.py           # Abstract base for all agents
│   ├── message.py              # Message format (incl. SACMP-ready signatures)
│   └── transport.py            # Future: handles async queue or bus
│
├── memory/
│   └── registry.py             # (Optional) memory or long-term storage
│
├── prompt_1.txt                # System prompt template (injects schema)
├── user_interface.py           # CLI or future API for user interaction
├── main.py                     # Manual A2A orchestrator chain
├── .env                        # OpenAI API Key and env config

---

## 🚀 Quick Start

### 1. Clone and setup

```bash
git clone https://github.com/your-org/ntsctAI-a2a.git
cd ntsctAI-a2a

2. Environment setup

Install dependencies:

pip install -r requirements.txt

Create .env:

OPENAI_API_KEY=your_openai_key_here

3. Run the demo

python main.py

You’ll be prompted for a natural language query. The system runs the following chain:

User → PlannerAgent → ElasticAgent → VizAgent → Chart Display


⸻

🧩 Example Queries

What are the top 5 servers with the highest packet loss?
Which IP has the most unique applications served?
List the top 3 clients generating DNS traffic to 8.8.8.8.


⸻

🔐 SACMP Compatibility (Planned)
	•	All messages support digital signatures per agent.
	•	Memory entries (e.g., vector results, plans) will be agent-signed.
	•	Replay protection, schema fingerprinting, and provenance are in scope.

⸻

🧱 Extending

Component	You can add…
ElasticAgent	Support for multiple backends (Splunk, Loki)
VizAgent	Graph export, summary tables, HTML reports
Message	signature, trace_id, or auth_context fields
Transport	Real A2A: Redis, MQTT, or REST messaging bus


⸻

🤝 License & Credits

MIT License
Inspired by ideas from MCP (Model Context Protocol) and A2A architectures.

⸻

📬 Contact

Maintainer: [Your Name]
Email: [your.email@example.com]
Project status: Research-grade, evolving toward production.

