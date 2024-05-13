from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'


class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

    # 检查 setup 字段必须以"?"结尾，会在 parse 生成实例化对象时生效
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field


output_parser = PydanticOutputParser(pydantic_object=Joke)
prompt_template = PromptTemplate(
    template="Tell me a joke.\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
print(prompt_template)
llm = OpenAI()
chain = prompt_template | OpenAI()
output = chain.invoke({})
print(output)
# >> {"setup": "Why don't scientists trust atoms?", "punchline": "Because they make up everything."}
print(output_parser.parse(output))
# >> Joke{setup='Why don't scientists trust atoms?' punchline='Because they make up everything.'}
