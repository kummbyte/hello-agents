from dotenv import load_dotenv
from hello_agents import CalculatorTool, HelloAgentsLLM, SimpleAgent


load_dotenv()

llm = HelloAgentsLLM()

agent = SimpleAgent(
    name="AI助手",
    llm=llm,
    system_prompt="你是一个有用的AI助手"
)

response = agent.run("请介绍你自己")
print(response)

calculator = CalculatorTool()

response = agent.run("请帮我计算 2 + 3 * 4")
print(response)

print(f"历史消息数:{len(agent.get_history())}")