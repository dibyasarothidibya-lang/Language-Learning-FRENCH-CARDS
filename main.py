
import os
import random
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas

BACKGROUND_COLOR = "#B1DDC6"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "data", "french_words.csv")
WORDS_TO_LEARN_FILE = os.path.join(SCRIPT_DIR, "data", "words_to_learn.csv")

# ---------------------------- DATA SETUP ------------------------------- #
try:
    data = pandas.read_csv(WORDS_TO_LEARN_FILE)
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv(DATA_FILE)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    if not to_learn:
        original_data = pandas.read_csv(DATA_FILE)
        to_learn = original_data.to_dict(orient="records")

current_card = {}


# ---------------------------- CARD MECHANICS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    if not to_learn:
        canvas.itemconfig(card_title, text="Completed!", fill="black")
        canvas.itemconfig(card_word, text="All words learned!", fill="black")
        canvas.itemconfig(card_background, image=card_front)
        return

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    if not current_card:
        return
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    if current_card and current_card in to_learn:
        to_learn.remove(current_card)
        df_to_learn = pandas.DataFrame(to_learn)
        df_to_learn.to_csv(WORDS_TO_LEARN_FILE, index=False)
    next_card()


new_word = next_card

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "card_front.png"))
card_back = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Clicking the card manually also flips it
canvas.bind("<Button-1>", lambda event: flip_card())

# Buttons
wrong_img = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "wrong.png"))
wrong_button = Button(
    image=wrong_img,
    highlightthickness=0,
    bd=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=next_card,
)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "right.png"))
right_button = Button(
    image=right_img,
    highlightthickness=0,
    bd=0,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=is_known,
)
right_button.grid(row=1, column=1)

next_card()

if __name__ == "__main__":
    window.mainloop()

