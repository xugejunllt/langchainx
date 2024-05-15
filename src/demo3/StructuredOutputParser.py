from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

response_schemas = [
    ResponseSchema(name="setup", description="question to set up a joke"),
    ResponseSchema(name="punchline", description="answer to resolve the joke")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
prompt_template = PromptTemplate(template="Tell me a joke\n{format_instructions}", input_variables=[], partial_variables={"format_instructions": output_parser.get_format_instructions()}, )

chain = prompt_template | OpenAI()
output = chain.invoke({})
print(output)
"""
```json
{
        "setup": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything."
}
``` 
"""
print(output_parser.parse(output))
"""
{
    "setup": "Why don't scientists trust atoms?",
    "punchline": "Because they make up everything."
}
"""
