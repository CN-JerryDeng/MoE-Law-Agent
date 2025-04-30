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

def easy_write(file_name='whole_log.txt',edit_method='a',content=''):
    with open(file_name,edit_method) as file:
        file.write(content)

def respond_and_log(model_name,prompt,request,file_name='whole_log.txt',edit_method='a'):
    content = model_response(model_name,prompt,request)
    easy_write(file_name,edit_method,content)

def Court_SIM():
    easy_write('whole_log.txt',edit_method='a','当前流程ID 0')
    process = 0
    #0 庭前准备：核对身份、宣布纪律、合议庭组成、询问回避 
    #1 法庭调查：原告陈述、被告答辩、举证质证
    #2 法庭辩论：双方发言、争议焦点
    #3 最后陈述：原被告最后意见）
    #4 调解阶段：询问调解意愿
    #5 宣判：当庭或择期
    #6 总结
    #庭前准备
    #if process == 0:    
