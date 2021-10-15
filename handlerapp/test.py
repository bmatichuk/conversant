import openai as ai

def chat(question,chat_log = None) -> str:
    print("input:----",question)
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nGPT-3:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0,
    presence_penalty=0.7, best_of=2,max_tokens=100,stop = "\nHuman: ")
    # print('response.choices[0].text:---------------', response.choices[0].text)
    print('answer',response.choices[0].text)
#
# def modify_start_message(chat_log,question,answer) -> str:
#     if chat_log == None:
#         chat_log = start_chat_log
#     chat_log += f"Human: {question}\nAI: {answer}\n"
#     # print('chat_log:---------',chat_log)
#     return chat_log

if __name__ == "__main__":
    ai.api_key = "sk-AeXpLitBfpAiHS8jwKg6KCcwsc6vd967Spyx0QK2"
    completion = ai.Completion()
    start_chat_log = """Human: Hello, I am Human.
    AI: Hello, human I am openai gpt3.
    Human: How are you?
    AI: I am fine, thanks for asking. 
    """
    question = ""
    print("\nEnter the questions to openai (to quit type \"stop\")")
    while True:
        question = input("Question:-- ")
        if question == "stop":
            break
        print("AI: ",chat(question,start_chat_log))