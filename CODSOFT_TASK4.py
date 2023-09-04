import random
import tkinter as tk
from tkinter import messagebox

def game(user, comp):
    if user == comp:
        return "It's a tie!"
    elif user == 'rock':
        if comp == 'scissor':
            return "You Win!"
        else:
            return "Computer wins!"
    elif user == 'paper':
        if comp == 'rock':
            return "You win!"
        else:
            return "Computer wins!"
    elif user == 'scissor':
        if comp == 'paper':
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid User Input"

def play_game():
    user_input = user_choice.get().lower()
    comp_input = random.choice(["rock", "paper", "scissor"])
    result = game(user_input, comp_input)
    result_label.config(text="Result: " + result)
    inputs_label.config(text="User Input: " + user_input.capitalize() + "\nComputer Input: " + comp_input.capitalize())

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and pack GUI elements
user_choice = tk.StringVar()
user_choice.set("rock")
user_label = tk.Label(root, text="Enter Rock/Paper/Scissor:")
user_label.pack()

user_entry = tk.Entry(root, textvariable=user_choice)
user_entry.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

inputs_label = tk.Label(root, text="User Input: \nComputer Input: ")
inputs_label.pack()

# Start the GUI event loop
root.mainloop()
