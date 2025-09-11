from utils.constants import TERMINAL_WIDTH

def seperator():
    print("="*TERMINAL_WIDTH)

def formatContent(content:str)->str:
    sentences = content.split(". ")
    for sentence in sentences:
        sentence.strip()
    sentences.pop()
    return "".join(sentence+". " for sentence in sentences)