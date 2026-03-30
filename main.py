# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from langchain_ollama.chat_models import ChatOllama


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    llm = ChatOllama(model="qwen3.5:4b")
    resp = llm.invoke("你能做什么")
    print(resp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
