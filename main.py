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
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(request)},
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
    with open(file_name,edit_method,encoding='utf-8') as file:
        file.write(content + '\n')

def respond_and_log(model_name,prompt,request,file_name='whole_log.txt',edit_method='a'):
    content = model_response(model_name,prompt,request)
    easy_write(file_name,edit_method,content)

def role_respond(role):
    with open(f'.\\role\\{role}\\prompt.txt', 'r', encoding='utf-8') as file:
            prompt = file.read()
    if role == 'Court Clerk':
        model_name = 'doubao-pro-32k-241215'
        request = open('whole_log.txt','r',encoding='utf-8').read()
        file_name = 'Court_log.txt'
    if role == 'Judge':
        model_name = 'deepseek-v3-250324'
        request = open('Court_log.txt','r',encoding='utf-8').read()
        file_name = 'Court_log.txt'
    if role == 'Plaintiff':
        model_name = 'deepseek-v3-250324'
        request = open('Court_log.txt','r',encoding='utf-8').read()
        file_name = 'whole_log.txt'
    respond_and_log(model_name,prompt,request,file_name)

def Court_SIM():
    process = 0
    #0 庭前准备：核对身份、宣布纪律、合议庭组成、询问回避 
    #1 法庭调查：原告陈述、被告答辩、举证质证
    #2 法庭辩论：双方发言、争议焦点
    #3 最后陈述：原被告最后意见）
    #4 调解阶段：询问调解意愿
    #5 宣判：当庭或择期
    #6 总结
    #庭前准备
    while process <6:
        if process == 0:    
            easy_write(content="书记员：1、未经法庭允许不得录音、录像、摄影；2、除本院因工作需要允许进入审判区的人员外，其他人员一律不准进入审判区；3、不得鼓掌、喧哗、吵闹以及实施其他妨碍审判活动的行为，未经审判长许可，不准发言、提问；4、旁听人员如对法庭的审判活动有意见，可在休庭或闭庭后，口头或书面向法庭指出；5、对于违反法庭规则的人，审判人员可以口头警告训诫，也可以没收录音、录像和摄影器材，责令退出；6、对哄闹、冲击法庭、侮辱、诽谤、殴打审判人员等严重扰乱法庭秩序的人，依法追究刑事责任，情节较轻的予以罚款；7、请关闭随身携带的手机、寻呼机。全体起立，请审判长、合议庭成员入庭。")
            role_respond('Court Clerk')
            respond_and_log('deepseek-v3-250324',
                            open(f'.\\role\\Judge\\prompt.txt','r',encoding='utf-8').read()
                            ,'\n 请依据案情进行开庭开场白，格式:法官：今天就原告XXX与被告XXX XXX纠纷一案，依法公开开庭审理。本案适用简易程序，由审判员独自审判，书记员担任记录。根据XXX的规定，当事人对审判人员、书记员有申请回避的权利。')
            role_respond('Court Clerk')
            process += 1
            continue
        if process == 1:
            respond_and_log('deepseek-v3-250324',
                            open(f'.\\role\\Plaintiff\\prompt.txt','r',encoding='utf-8').read()
                            ,'\n 请依据案情进行原告陈述，包括“诉讼请求”、“事实和理由”等')
            role_respond('Court Clerk')

Court_SIM()
