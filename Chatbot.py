import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?", ] # แก้ไขให้เป็น list
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", ] # แก้ไขให้เป็น list
    ],
    [
        r"what is your name?",
        ["I am a chatbot.", ] # แก้ไขให้เป็น list
    ],
    [
        r"how are you \??", #เพิ่ม ? เพื่อให้ครอบคลุมคำว่า how are you
        ["I'm doing well, thank you!", "I'm fine, thanks.", ] # แก้ไขให้เป็น list
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem.", ] # แก้ไขให้เป็น list
    ],
    [
        r"I (.*) need (.*)",
        ["Why do you need %2?", ] # แก้ไขให้เป็น list
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. See you later.", ] # แก้ไขให้เป็น list
    ],
    [
        r"(.*)",
        ["I'm not sure I understand.", "Could you please rephrase that?", ] # แก้ไขให้เป็น list
    ],
]

def chat():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chat()
