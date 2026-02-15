import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0


def rock():
    play("Rock")


def paper():
    play("Paper")


def scissors():
    play("Scissors")


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text="You chose: " + user_choice)
    comp_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie", fg="blue")

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        result_label.config(text="You Win", fg="green")
        user_score = user_score + 1

    else:
        result_label.config(text="Computer Wins", fg="red")
        computer_score = computer_score + 1

    score_label.config(
        text="Score  You: " + str(user_score) +
             "   Computer: " + str(computer_score)
    )


def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="")
    comp_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Score  You: 0   Computer: 0")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x330")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Rock Paper Scissors",
                 font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

rock_btn = tk.Button(frame, text="Rock", width=10, bg="#ffb3ba", command=rock)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(frame, text="Paper", width=10, bg="#bae1ff", command=paper)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(frame, text="Scissors", width=10, bg="#baffc9", command=scissors)
scissors_btn.grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="", font=("Arial", 11), bg="#f0f0f0")
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 11), bg="#f0f0f0")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#f0f0f0")
result_label.pack(pady=8)

score_label = tk.Label(root, text="Score  You: 0   Computer: 0",
                       font=("Arial", 11), bg="#f0f0f0")
score_label.pack(pady=5)

reset_btn = tk.Button(root, text="Reset Game", width=15, bg="orange", command=reset_game)
reset_btn.pack(pady=8)

root.mainloop()
