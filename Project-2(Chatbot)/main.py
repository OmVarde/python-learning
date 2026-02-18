# project-2
# In this project we will build a mini AI chatbot that can interact with users 
#The chatbot will understand simple messages like "hello"
# "motivate me", or "python" and respond with friendly intelligent answers
import datetime
import time

name = input("Welcome, Enter your Name:")
presentHour = datetime.datetime.now().hour
time.sleep(2)

if 5<= presentHour <= 11:
    print("Good morning, ",name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ",name)
elif 17 <= presentHour <= 20:
    print("Good evening, ",name)
else:
    print("Good night, ",name)
    




print("Hello, everyone I am Om's study buddy! \n You can talk to me.\n Type 'bye' anytime to exit")
responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine.Thank you",
    "who are you": "I am your chatbot ",
    "motivate me": "Keep Going, Every bug you fixes makes you a better coder",
    "happy": "Great to hear that",
    "bye":"Take care, Good day"
}
# method functions to get response of Chatbox
def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    time.sleep(2)
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to tell that yet am still learning"
# take user input 
while True:
    userInput = input("Enter your question:")
    reply= getResponseBot(userInput)
    print("Bot response:",reply)

    if "bye" in userInput.lower():
        break   
