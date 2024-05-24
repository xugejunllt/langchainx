from langchain.output_parsers.openai_tools import JsonOutputToolsParser
from langchain_core.messages import HumanMessage, FunctionMessage
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

# messages = [{"role": "user", "content": "what's the beijing's weather like in 2024-01-01"}]


# langchain_core.utils.function_calling.convert_to_openai_function()
class GetWeather(BaseModel):
    """Get the weather for a specified location on a specified date"""
    location: str = Field(description="The city and state, e.g. 北京")
    date: str = Field(description="the date to get weather, e.g. 2024-01-01")


def get_weather(date, location):
    print("after query，{}{}'s weather is 20℃".format(date, location))
    return "20℃"


parser = JsonOutputToolsParser()
chain = ChatOpenAI().bind_tools([GetWeather]) | parser


"""
[{'type': 'GetWeather', 'args': {'location': '北京', 'date': '2024-01-01'}}]
"""

messages = []
messages.append(HumanMessage(content="what's the beijing's weather like in 2024-01-01?"))
output = chain.invoke(messages)
print(output)

# item = output[0]
# args = item['args']
# location = args["location"]
# date = args["date"]

# 使用列表推导式和解包来直接获取值
location, date = next(item['args'].values() for item in output if 'args' in item)
# 打印结果
print(f"Location: {location}, Date: {date}")

messages.append(FunctionMessage(content=get_weather(date, location), name='get_weather'))

chain2 = ChatOpenAI()
print(chain2.invoke(messages))
