from sys import displayhook
x
def chatbot( 
    
print("chatbot:hi!i'm your simple chatbot.ask me anything or type 'exit'end the chat.")
            
responses={
           "hello"! how can i help you today
           "how are you?":im doing well,thank you for asking
           "what,s your name?":my name is chatbot
           "bye":goodbye!have a nice day
           "default":i'm sorry,i don't understand what you'r saying


while Ture:
    user_input=input("you:").strip(). lower()#Get user input and strip
    if user_input == "exit":
        print("chatbot:goodbye!")
        break
    #respond basing on predefined responses or use a default mssage
    response=responses.get(user_input,"I'M sorry,i don,t understand that.can you rephrase?")
    print(f"chatbot:"{response}")
#run the chatbot
if__name__=="__main__":
           chatbot()