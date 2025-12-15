from agent.llm import ask_llm
from agent.memory import Memory

memory = Memory()

def start_agent():
    while True:
        user_input = input("User > ")

        if user_input.lower() == "exit":
            break

        memory.add(user_input)
        response = ask_llm(user_input, memory.get())
        print("Agent >", response)
