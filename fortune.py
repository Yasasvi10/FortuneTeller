print("Welcome to Vejendla Yasasvi Sai Naga Lakshmi's Fortune Teller (21JE1038)")

mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("Your fortune: Great things await you, Yasasvi! Keep spreading joy!")
elif mood == "sad":
    print("Your fortune: Tough times don’t last. You are stronger than you think.")
elif mood == "neutral":
    print("Your fortune: Stay curious and something wonderful might happen.")
else:
    print("Your fortune: Sorry, I can't predict a fortune for that mood.")
