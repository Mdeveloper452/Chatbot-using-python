from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('SimpleBot')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with the English language corpus
trainer.train('chatterbot.corpus.english')

# Start the conversation
print("Hello, I am SimpleBot. Type something to begin talking to me!")

while True:
    try:
        user_input = input("You: ")
        bot_response = chatbot.get_response(user_input)
        print(f"SimpleBot: {bot_response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nGoodbye!")
        break
