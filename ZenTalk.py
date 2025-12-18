import random  #imported ramdom function to select random movies
#created a list to store chat data 
chat_history = []
#created some predefined questions and answer in the form of functions 
def movies(statement):
    statement = statement.lower()
    movies = {
        "comedy": [
            "Jathiratnalu","Ee nagaraniki em ayyindi","Mathuvadalara","F2","Single",
            "Middle class Melodies","Kevukeka","Jombireddy","Shubam","Dj tillu"
        ],
        "horror": [
            "It","Odela","Virupaksha","Masuda","Pindam","Raju Gari Gadhi",
            "Geethanjali","Mangalavaram","Nextnuvve","Bhagamathi","DDreturns"
        ],
        "action": [
            "Veerasimhareddy","Akhanda","Mirchi","Athadu","Gunturkaram","Hit3",
            "Pokiri","OG","Salaar","Saaho","Bhemlanaik","Hanuman","RRR","KGF",
            "Bahubali","Devara"
        ],
        "romantic": [
            "Kushi","Fidaa","NinuKori","Sitaramam","Majili","Srimanthudu","Orange",
            "A AA","Thandel","Hi naana","Life is beautiful","Gangleader",
            "Aravindasametha","Hello","Familystar","Geethagovindam"
        ]
    }
#used loop here to check user input is in the above dictionary
    for genre in movies:
        if genre in statement:
            return "🎬 You should watch: " + random.choice(movies[genre])


def medical_advices(statement):
    statement = statement.lower()
    tips = {
        "fever": "You have fever less than 100°F you can use Dolo-650. If higher than 100°F consult a doctor.",
        "headache": "Take Saridon tablet and take rest. If pain continues consult doctor.",
        "cold": "Drink warm liquids and take steam every 2 hours.",
        "stomach": "Avoid spicy food and eat light meals.",
        "back": "Sit correctly and avoid lifting heavy objects.",
        "body": "Take proper rest and avoid hard work."
    }

    for key in tips:
        if key in statement:
            return tips[key]


def technology(statement):
    statement = statement.lower()
    tech = {
        "project": "Python projects: Calculator, Bank Management System, Rock Paper Scissors, Even/Odd checker",
        "variable": "A variable is a container used to store data. Example: name = 'Harsh'",
        "use python": "Python is used in Data Science, Machine Learning, Web Development, Automation.",
        "learn python": "You can learn from SathvikSolutions (paid) or Bro Code (YouTube)."
    }

    for key in tech:
        if key in statement:
            return tech[key]


def places(statement):
    statement = statement.lower()
    places = {
        "hyderabad": "Tank Bund, Charminar, Golconda Fort, Ramoji Film City",
        "india": "Taj Mahal, Red Fort, Mysore Palace, Goa, Tirumala",
        "country": "Italy, France, Spain, Thailand, Greece",
        "travel": "Visit Tirumala first, then Tiruvannamalai."
    }

    for key in places:
        if key in statement:
            return places[key]


def greetings(statement):
    statement = statement.lower()
    greet = {
        "hello": "Hi I'm Harshu! How can I help you?",
        "how are you": "I'm good 😊 What about you?",
        "robot": "Yes! I'm definitely a robot 🤖",
        "ghost": "I'm a friendly ghost 👻"
    }

    for key in greet:
        if key in statement:
            return greet[key]


def costumes(statement):
    statement = statement.lower()
    costumes = {
        "traditional": "Traditional wear: Dhoti, Kurta Pajama, Sherwani",
        "lipstick": "Try MAC Ruby Woo, Clinique Black Honey, Dior Rouge 999",
        "perfume": "Bella Vita Honey or perfumes from Westside",
        "outfit": "White, Grey, Navy Blue, Black combinations look great"
    }

    for key in costumes:
        if key in statement:
            return costumes[key]


# MAIN LOOP
while True:
    print('==============================================================================================')
    print('   ------------------------------ WELOCME TO ZENTALK ------------------------------')
    print('==============================================================================================')
    print("-------------------- zentalk can made Mistakes --------------------")
    statement = input("\nAsk here I'm zentalk: ").lower()

    # EXIT COMMAND
    if statement in ["bye", "exit", "quit"]:
        print("👋 Bye! Nice talking to you.")
        break

    # SHOW HISTORY
    if statement == "history":
        print("\n📜 Chat History:")
        for chat in chat_history:
            print(chat)
        continue

    response = (
        movies(statement)
        or medical_advices(statement)
        or technology(statement)
        or places(statement)
        or greetings(statement)
        or costumes(statement)
        or "❓ Sorry, I didn't understand that."
    )

    print(response)

    chat_history.append("You: " + statement)
    chat_history.append("Bot: " + response)
