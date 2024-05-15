from openai import OpenAI

# import os
# os.environ['OPENAI_API_KEY'] = 'sk-tmoDMPRuK9meGez2A28rvnSS86QzUuwC5aQDdQnjvRcuKclL'
# os.environ['OPENAI_API_BASE'] = 'https://api.fe8.cn/v1'

client = OpenAI(
    api_key = "sk-tmoDMPRuK9meGez2A28rvnSS86QzUuwC5aQDdQnjvRcuKclL",
    base_url = "https://api.fe8.cn/v1"
)
# client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",

  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://scm-dam.oss-cn-shanghai.aliyuncs.com/image/orgimg/baozun/ikea/20240428162130/R20542/R20542-A.jpg?etag=1714292491472",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])