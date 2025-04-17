import random

print("Welcome to Vejendla Yasasvi Sai Naga Lakshmi's Fortune Teller (21JE1038)")

mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        "Keep shining, Yasasvi! Your happiness is beautiful;)",
        "Joy suits you perfectly, Yasasvi! You will have a crazy day today.",
        "The world smiles with you today, Yasasvi!"
    ],
    "sad": [
        "Hang in there. Better days are coming.",
        "Even the darkest night will end and the sun will rise.",
        "Yasasvi believes in you! Stay strong and you will shine"
    ],
    "neutral": [
        "It’s a good day to try something new.",
        "Neutral today, legendary tomorrow.",
        "Balance is a strength which you will use to do great things today!"
    ],
    "stressed": [
        "Take a deep breath. You've got this.",
        "Stress is temporary, your strength is not.",
        "Be kind to yourself today."
    ]
}

if mood in fortunes:
    print("Your fortune: ")
    print(random.choice(fortunes[mood]))
else:
    print("Your fortune: Sorry, I don't have a fortune for that mood.")