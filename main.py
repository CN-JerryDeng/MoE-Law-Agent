import time
from openai import OpenAI

#OpenAI 基础配置
client = OpenAI(
    api_key = "342a330c-8a87-48c7-9d57-876f7270dac6",
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)

#model_response函数 用于获取模型回复 格式(模型id,提示词,user输入)
def model_response(model_name,prompt,request):              
    completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content":prompt},
            {"role": "user", "content":request},
        ],
    )
    #获取结束原因
    finish_reason = completion.choices[0].finish_reason     
    while True:
        if finish_reason == "stop":
            break
        else:
            print(f"生成被中止，原因：{finish_reason}")
    return completion.choices[0].message.content
