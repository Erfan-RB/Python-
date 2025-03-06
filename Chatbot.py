import openai

openai.api_key = "Please enter your api here"
#create api from this site : https://platform.openai.com/account/api-keys
def chat_with_gpt(prompt):
    respone = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        message=[{"role": "user", "content": prompt}]
    )
    
    RETURN RESPONE.CHOICES[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        respone = chat_with_gpt(user_input)
        print("Chatbot: ", respone)
