from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

THEME_COLOR = "#375362"

# Convert data into Question objects
question_bank = [Question(q["text"], q["answer"]) for q in question_data]
quiz = QuizBrain(question_bank)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Quiz App")
window.config(padx=20, pady=20, bg=THEME_COLOR)

# Score Label
score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
score_label.grid(row=0, column=1)

# Canvas for question text
canvas = Canvas(width=300, height=250, bg="white")
question_text = canvas.create_text(
    150, 125,
    width=280,
    text="Question goes here",
    font=("Arial", 16, "italic"),
    fill=THEME_COLOR
)
canvas.grid(row=1, column=0, columnspan=2, pady=50)

# Button images
true_img = PhotoImage(file="images/true.png")
false_img = PhotoImage(file="images/false.png")

# Buttons
def true_pressed():
    give_feedback(quiz.check_answer("True"))

def false_pressed():
    give_feedback(quiz.check_answer("False"))

true_button = Button(image=true_img, highlightthickness=0, command=true_pressed)
true_button.grid(row=2, column=0)

false_button = Button(image=false_img, highlightthickness=0, command=false_pressed)
false_button.grid(row=2, column=1)

# ---------------------------- LOGIC ------------------------------- #
def get_next_question():
    canvas.config(bg="white")
    if quiz.still_has_questions():
        q_text = quiz.next_question()
        canvas.itemconfig(question_text, text=q_text)
        score_label.config(text=f"Score: {quiz.score}")
    else:
        canvas.itemconfig(question_text, text="You've completed the quiz!")
        true_button.config(state="disabled")
        false_button.config(state="disabled")

def give_feedback(is_right):
    canvas.config(bg="green" if is_right else "red")
    if is_right:
        quiz.score += 1
        score_label.config(text=f"Score: {quiz.score}")
    window.after(1000, get_next_question)

get_next_question()

window.mainloop()
