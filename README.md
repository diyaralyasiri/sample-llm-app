Agentic LLM App with OpenTelemetry (OTel) Instrumentation

This is a sample project demonstrating how to build an Agentic LLM application using LangChain, instrumented with OpenTelemetry for full end-to-end observability. The app uses a FastAPI server, integrates OpenAI (or another LLM provider), and exports traces to Splunk Observability Cloud.

## 🧰 Prerequisite: Run a Local Splunk OTel Collector

This application requires a **Splunk OpenTelemetry Collector** to be running on your local machine to receive and forward telemetry data to Splunk Observability Cloud.

If you're running this on your personal machine, the easiest way to start a local collector is via Docker:

```bash
docker run --rm -it \
  -e SPLUNK_ACCESS_TOKEN=your-splunk-token \
  -e SPLUNK_REALM=us1 \
  -e SPLUNK_MEMORY_TOTAL_MIB=512 \
  -p 4317:4317 \
  -p 4318:4318 \
  --name splunk-otel-collector \
  quay.io/signalfx/splunk-otel-collector:latest

  This command pulls the latest collector image and runs it in the foreground, listening for OTLP data on ports 4317 (gRPC) and 4318 (HTTP). Update the access token and realm to match your Splunk environment.

Ensure the .env file in your project has the same token and realm so the telemetry can be exported successfully.


You can reference the Splunk documentation to learn more about setup and configuration:  
  [Install the Splunk OpenTelemetry Collector](https://docs.splunk.com/Observability/gdi/opentelemetry/install-the-collector.html)

What This App Does
This project builds a tool-using LLM agent capable of performing basic arithmetic operations (add, subtract, multiply, divide) by calling programmatic tools instead of doing the math itself. The app is fully observable with OpenTelemetry, enabling insights into how prompts are processed, tools are invoked, and responses are generated.

Technologies Used
- FastAPI
- LangChain
- OpenAI (via langchain_openai)
- OpenTelemetry
- Splunk Observability Cloud
- Pipenv for dependency management

Project Structure
sample-llm-app/
├── agent.py           # Defines arithmetic tools and the LLM agent using LangChain
├── main.py            # FastAPI app that wraps the agent
├── telemetry.py       # Sets up OpenTelemetry exporters (e.g. OTLP to Splunk)
├── Pipfile            # Project dependencies
├── .env               # API keys and tokens (not included in repo)
└── README.md          # This file

Prerequisites
- Python 3.9+
- pipenv installed:
pip install pipenv

Setup Instructions

1. Clone the Repository
git clone https://github.com/your-org/sample-llm-app.git
cd sample-llm-app

2. Install Dependencies
pipenv install

This will install all required packages, including:
- fastapi, uvicorn
- langchain, langchain_openai
- openai
- opentelemetry-api, opentelemetry-sdk, opentelemetry-exporter-otlp
- python-dotenv

3. Create a .env File
OPENAI_API_KEY=your-openai-api-key
SPLUNK_REALM=your-splunk-realm
SPLUNK_ACCESS_TOKEN=your-splunk-token

If using another LLM provider like Anthropic or Mistral, update the ChatOpenAI implementation in agent.py.

4. Start the App
pipenv run uvicorn main:app --reload --log-level debug

Then open your browser to:
http://127.0.0.1:8000/docs

How to Use the Agent
Send a request via the FastAPI endpoint or from within Python:
agent_executor.invoke({"input": "What is 10 times 8 minus 4?"})

Logs are saved to tmp.log.

Observability with OpenTelemetry
The app instruments both the FastAPI server and LangChain agent with OpenTelemetry. Trace data is exported to Splunk via OTLP.

Telemetry setup is handled in telemetry.py. Be sure your network allows outbound access to:
https://ingest.<SPLUNK_REALM>.signalfx.com/v2/trace

Extending the App
- Add more tools (e.g., currency conversion, weather info).
- Replace the arithmetic agent prompt to support more domains.
- Enable metrics/logs in addition to traces for full OTel coverage.

Example Trace in Splunk
- View traces by filtering for service.name="llm-arithmetic-agent"
- Drill into spans to see:
- Input prompt
- Tool selected
- LLM usage details (token counts, latency)

Need Help?
- LangChain Docs: https://docs.langchain.com
- OTel Python SDK: https://opentelemetry.io/docs/instrumentation/python/
- Splunk Observability: https://docs.splunk.com/Observability

Cleanup
To shut down:
CTRL+C  # to stop uvicorn
deactivate && pipenv --rm




License
MIT License 
