
def chatbot():
    print("Welcome to Python Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I'm fine, thank you!")

        elif "your name" in user_input:
            print("Bot: I am a Python chatbot.")

        elif "python" in user_input:
            print("Bot: Python is a popular programming language.")

        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")

chatbot()
