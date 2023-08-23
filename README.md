# meeting-summary

## 仓库简介：
输入会议文字内容（不限长度），基于chatgpt自动生成会议纪要。格式美观。

 ## 使用方法：
 1. 在目录下新建production.env文件，填入
```
OPENAI_API_KEY=<你的openai api key>
API_BASE=<openai api的请求断点>
```
2. 复制会议文字内容至meeting_content.txt中，运行main.py.

3. 在目录summary.txt中查看生成的会议纪要。


## 算法流程：
1. 使用gpt3.5对不同chunk的内容进行会议纪要，最后将不同chunk生成的会议纪要放在一起总结
2. 使用gpt4美化输出格式。
