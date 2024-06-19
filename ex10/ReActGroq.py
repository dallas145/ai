import os
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

groq_key = os.environ.get("GROQ_API_KEY")

tools = [TavilySearchResults(max_results=1)]

prompt = hub.pull("hwchase17/react")

llm = ChatGroq(api_key=groq_key)

agent = create_react_agent(llm, tools, prompt)

agent_excuter = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_excuter.invoke({"input": "許氏注音用多少個按鍵輸入中文？用中文回答。"})