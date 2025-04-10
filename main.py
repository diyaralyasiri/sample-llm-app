from fastapi import FastAPI
from dotenv import load_dotenv
from otel import setup_openllmetry
import agent
# from langchain_community.callbacks.manager import get_openai_callback


load_dotenv()
app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@app.get("/calculate")
def question(
    prompt: str | None = "tell me about Dubai?"):
    response = agent.agent_executor.invoke({"input": prompt})
    # response=agent.ask_question(prompt)
    
    return {"result": response}

setup_openllmetry(app)