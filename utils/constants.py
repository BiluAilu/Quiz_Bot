from typing import List

categories=["Programming","Networking","Other"]
levels=["easy","medium","hard"]



def customized_messages(score):
    if score in range(0,3):
        return "Don't worry, everyone starts somewhere! Keep exploring, and you'll master these questions in no time."
    elif score in range(3,5):
        return "Great job! You're on the right track. Keep challenging yourself, and there's no limit to what you can achieve!"
    elif score in range(5,5):
        return "Wow! Perfect score! You're a true Quiz Master! 🏆 Your knowledge knows no bounds. Can anyone top your brilliance?"

