import tkinter as tk
from tkinter import messagebox

questions = [
    "Capital of France?",
    "Red Planet?",
    "Largest mammal?",
    "Python is a ___ language?",
    "Boiling point of water?"
]

options = [
    ["Berlin", "Paris", "Rome", "Madrid"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Elephant", "Blue Whale", "Horse", "Dog"],
    ["Compiled", "Interpreted", "Machine", "Assembly"],
    ["90°C", "80°C", "100°C", "120°C"]
]

answers = [1, 1, 1, 1, 2]

user_answers = []
index = 0

root = tk.Tk()
root.title("MCQ Test")
root.geometry("250x250")

choice = tk.IntVar()

question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=10)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=choice, value=i)
    rb.pack(anchor="w")
    radio_buttons.append(rb)

def load_question():
    choice.set(-1)
    question_label.config(text=questions[index])
    for i in range(4):
        radio_buttons[i].config(text=options[index][i])

def next_question():
    global index
    user_answers.append(choice.get())
    index += 1

    if index < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    score = 0
    mistakes = ""

    for i in range(len(questions)):
        if user_answers[i] == answers[i]:
            score += 1
        else:
            mistakes += (
                f"\nQ{i+1}: {questions[i]}\n"
                f"Your answer: {options[i][user_answers[i]] if user_answers[i] != -1 else 'Not answered'}\n"
                f"Correct answer: {options[i][answers[i]]}\n"
            )

    messagebox.showinfo(
        "Result",
        f"Score: {score}/{len(questions)}\n\nMistakes:{mistakes if mistakes else '\nNone!'}"
    )
    root.destroy()

next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack(pady=20)

load_question()
root.mainloop()
