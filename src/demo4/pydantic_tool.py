from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_openai import ChatOpenAI
from langchain_community.utils.openai_functions import (
    convert_pydantic_to_openai_function
)
from langchain_core.utils.function_calling import (
    convert_to_openai_function
)

import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'


# langchain_core.utils.function_calling.convert_to_openai_function()
class GetWeather(BaseModel):
    """Get the weather for a specified location on a specified date"""
    location: str = Field(description="The city and state, e.g. 北京")
    date: str = Field(description="the date to get weather, e.g. 2024-01-01")


print(convert_to_openai_function(GetWeather))

parser = JsonOutputFunctionsParser()
chain = ChatOpenAI().bind(functions=[convert_to_openai_function(GetWeather)]) | parser
output = chain.invoke("what's the beijing's weather like in 2024-01-01?")
print(output)
"""
{'location': '北京', 'date': '2024-01-01'}
"""
