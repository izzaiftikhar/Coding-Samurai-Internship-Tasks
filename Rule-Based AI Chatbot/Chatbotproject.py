# TASK 1: Basic Chatbot 
# Goal: Build a simple rule-based chatbot. 
# Scope: 
# ● Input from user like: "hello", "how are you", "bye". 
# ● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!". 
# Key Concepts Used: if-elif, functions, loops, input/output. 

# Welcome message
def chatbot():
    print("Welcome To AI Chatbot!")
    print('Type "bye" to exit.\n')

# Main chatbot loop
    while True:
        user = input("You: ").lower()

# Checks user messages and responses
        if user == "hello" or user == "hi" or user == "hey":
            print("Chatbot: Hi, Nice to meet you!")
        elif user == "how are you":
            print("Chatbot: I'm fine, Thanks!")
        elif user == "what is your name":
            print("Chatbot: My name is Python Chatbot")
        elif user == "what can you do":
            print("Chatbot: I can chat with you and answer your queries")
        elif user == "what is your favorite color":
            print("Chatbot: My favorite color is blue")
        elif user == "thanks":
            print("Chatbot: You're Welcome")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break 
        else:
            print("Chatbot: I'm sorry, I don't understand that")

#Exit chatbot
chatbot()




