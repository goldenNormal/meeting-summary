
def read_txt(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        text = f.read()
    return text

def write_txt(file_path,text):
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(text)

