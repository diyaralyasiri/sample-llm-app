# from openai import OpenAI  ## testing default OpenAI APIs
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.callbacks import FileCallbackHandler
from langchain_openai import ChatOpenAI
# from langchain_community.callbacks.manager import get_openai_callback


from dotenv import load_dotenv
load_dotenv()

# llm_openai=OpenAI() ## default OpenAI API test
llm_chatopenai=ChatOpenAI(stream_usage=True)

# ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        (
            
            "You are a basic arithmetic assitant system. For arithmetic questions In "
            "order to ensure the mathematical correctness, be sure to utilize"
            " the tools provided to you, as required. Ensure to convert"
            " provided numbers to decimal values before calling any tool. Your arithmetic responses"
            " must be solely a number calculated using the provided"
            "tools, even for the most trivial of operations.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# Tools
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds the two given numbers `a` and `b` and returns the sum."""
    return a + b


@tool
def subtract_numbers(a: int, b: int) -> int:
    """Subtracts the second number `b` from the first number `a` and returns the difference. In mathematical terms, this is `a - b`."""
    return a - b


@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies the two given numbers `a` and `b` and returns the product."""
    return a * b


@tool
def divide_numbers(a: int, b: int) -> float:
    """Divides the first number `a` by the second number `b` and returns the
    quotient."""
    return a / b


tools = [add_numbers, subtract_numbers, multiply_numbers, divide_numbers]


agent = create_tool_calling_agent(llm_chatopenai, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, callbacks=[FileCallbackHandler("tmp.log")]
)

### unused OpenAI API test function
# def ask_question(question):
#     completion = llm_openai.chat.completions.create(
#        model="gpt-3.5-turbo",
#        messages=[
#            {"role": "user", "content": question}
#        ]
#    )
#     return completion.choices[0].message.content

