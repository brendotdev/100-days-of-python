from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from html import unescape

THEME_COLOR = "#375362"

# Build question bank
question_bank = [
    Question(unescape(q["question"]), q["correct_answer"])
    for q in question_data
]

quiz = QuizBrain(question_bank)

# UI setup
window = Tk()
window.title("Quiz Game")
window.config(padx=20, pady=20, bg=THEME_COLOR)

score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
score_label.grid(row=0, column=1)

canvas = Canvas(width=300, height=250, bg="white")
question_text = canvas.create_text(
    150, 125,
    width=280,
    text="Question here",
    font=("Arial", 16, "italic"),
    fill=THEME_COLOR
)
canvas.grid(row=1, column=0, columnspan=2, pady=50)

true_img = PhotoImage(file="images/true.png")
false_img = PhotoImage(file="images/false.png")

def give_feedback(is_right):
    canvas.config(bg="green" if is_right else "red")
    if is_right:
        quiz.score += 1
        score_label.config(text=f"Score: {quiz.score}")
    window.after(1000, get_next_question)

def true_pressed():
    give_feedback(quiz.check_answer("True"))

def false_pressed():
    give_feedback(quiz.check_answer("False"))

true_button = Button(image=true_img, highlightthickness=0, command=true_pressed)
true_button.grid(row=2, column=0)

false_button = Button(image=false_img, highlightthickness=0, command=false_pressed)
false_button.grid(row=2, column=1)

def get_next_question():
    canvas.config(bg="white")
    if quiz.still_has_questions():
        q_text = quiz.next_question()
        canvas.itemconfig(question_text, text=q_text)
    else:
        canvas.itemconfig(question_text, text="You've completed the quiz!")
        true_button.config(state="disabled")
        false_button.config(state="disabled")

get_next_question()

window.mainloop()
