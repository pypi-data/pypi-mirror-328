import tkinter as tk
import random
import os

# Sample Bornvita Brainrot Quotes
BRAINROT_CONTENT = [
    "Drink Bornvita, Gain Infinite Wisdom 🧠",
    "Bornvita: The Cure for Low IQ! 🚀",
    "Only Legends Drink Bornvita 💪",
    "Bornvita: Secret to Becoming a 200 IQ Sigma 🦉",
    "One Sip, Infinite Knowledge 📚"
]

def generate_brainrot():
    """Generates a full-screen Bornvita brainrot message."""
    root = tk.Tk()
    root.title("Bornvita Brainrot")
    root.attributes('-fullscreen', True)
    root.configure(bg="black")

    # Randomly pick a message
    message = random.choice(BRAINROT_CONTENT)

    label = tk.Label(root, text=message, font=("Comic Sans MS", 40, "bold"),
                     fg="orange", bg="black", wraplength=1000)
    label.pack(expand=True)

    # Close on any key press
    root.bind("<Key>", lambda e: root.destroy())
    root.bind("<Button-1>", lambda e: root.destroy())

    root.mainloop()
