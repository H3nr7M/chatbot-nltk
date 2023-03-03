import nltk
from nltk.chat.util import Chat, reflections

# define a list of patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!"]),
    (r"what is your name?", ["My name is Chatbot.", "I'm Chatbot."]),
    (r"how are you?", ["I'm good, thanks.", "I'm doing well."]),
    (r"what can you do?", ["I can answer your questions.", "I can help you with things."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!"]),
]

# create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

# start the chat
chatbot.converse()
