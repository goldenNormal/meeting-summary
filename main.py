import dotenv
dotenv.load_dotenv('./production.env')
from utils import *
system_prompt = """请你想象你是一个专业的会议记录员，你的任务是在一场重要会议中，记录下关键讨论和决策，生成一份会议纪要。请确保你的记录既准确又全面，包括每个发言者的主要观点，讨论的主题，以及最后达成的共识。"""

from utils_llm_models import *

llm = LLM(new_gpt35())


meeting_content = read_txt('./meeting_content.txt')

meeting_lines = meeting_content.split('\n')
text = ''
new_text = ''
Sum = []
for i,line in enumerate(meeting_lines):
    text += line
    text += '\n'
    if get_token_cnt(text) > 14000:
        new_text += line
        new_text += '\n'
    if get_token_cnt(text) > 15000:
        llm.add_system(system_prompt)
        llm.add_human(f"会议内容如下：\n```{text}```")
        
        summary_part = llm.get_time_cost_reply()
        Sum.append(summary_part)
        text = new_text
        new_text = ''
        llm.clear()



if len(Sum) == 0:
    llm.add_system(system_prompt)
    llm.add_human(text)
    summary_part = llm.get_time_cost_reply()
    sum_all = summary_part
else:
    llm.add_system('您将看到来自同一会议不同部分的会议纪要，您的任务是将这些会议纪要内容进行整合以形成一个连贯、完整的会议总结。请尽可能地确保所有重要的讨论点和结论都被包含在内')
    input_text = ''
    for i in range(len(Sum)):
        input_text+=f'# 第{i+1}部分：\n'
        input_text +="```" +Sum[i]+"```"
        input_text += '\n'
    llm.add_human(input_text)
    sum_all = llm.get_time_cost_reply()

gpt4 =LLM(new_gpt4())
gpt4.add_system('请使用你的语言处理和设计能力，对以下的文字内容进行结构和排版的优化。我们的目标是提高其视觉吸引力和阅读舒适度。请确保你的修改能使最终的结果既美观又直观，同时也易于理解和阅读。你可以考虑使用段落分割、标题和子标题、列表、强调等元素来增强文本的结构和清晰度。')
gpt4.add_human('文字内容:\n```'+sum_all+'```')
beautify_sum_all = gpt4.get_time_cost_reply()

write_txt('summary.txt',beautify_sum_all)
    


