from dotenv import load_dotenv
from my_llm import MyLLM

load_dotenv()

# 使用项目的 ModelScope 兼容客户端
llm = MyLLM(provider="modelscope")

# 后续调用方式完全不变
messages = [{"role": "user", "content": "你好！"}]
for _ in llm.think(messages):
    pass
