# Import the necessary libraries
from tkinter import *
import pandas as pd
import random

# Create an empty dictionary to hold the current flashcard and a dictionary to hold the flashcards to review
current_flashcard = {}
review = {}

# Try to read the flashcards from a review file; if the file is not found, load the flashcards from a data file
try:
    data = pd.read_csv("data/review_words.csv", encoding="latin1")
except FileNotFoundError:
    word_data = pd.read_csv("data/icelandic_words.csv", encoding="latin1")
    print(word_data)
    review = word_data.to_dict(orient="records")
else:
    review = data.to_dict(orient="records")

# ---------- Functions ---------- #

# Function to display the next flashcard
def next_flashcard():
    global current_flashcard, card_view_time
    # Cancel the current flashcard display
    window.after_cancel(card_view_time)
    # Choose a new random flashcard and display it on the front of the card
    current_flashcard = random.choice(review)
    canvas.itemconfig(flashcard_title, text="Icelandic", fill="black")
    canvas.itemconfig(flashcard_word, text=current_flashcard["Icelandic"], fill="black")
    canvas.itemconfig(flashcard_background, image=front_image)
    # Set a timer to flip the flashcard after 4.5 seconds
    card_view_time = window.after(4500, func=flip_flashcard)


# Function to flip the flashcard and display the English word on the back of the card
def flip_flashcard():
    canvas.itemconfig(flashcard_title, text="English", fill="white")
    canvas.itemconfig(flashcard_word, text=current_flashcard["English"], fill="white")
    canvas.itemconfig(flashcard_background, image=back_image)


# Function to mark the current flashcard as correct and remove it from the review list
def correct_flashcard():
    review.remove(current_flashcard)
    print(len(review))
    # Save the updated review list to the review file
    data = pd.DataFrame(review)
    data.to_csv("data/review_words.csv", index=False)
    # Display the next flashcard
    next_flashcard()


# ---------- GUI setup ---------- #

# Create the main window for the flashcard program
window = Tk()
window.title("Icelandic-English Flashcards")
window.config(padx=50, pady=50, bg="#F5F5DC")

# Load the images for the front, back, wrong and correct cards
front_image = PhotoImage(file="images/front.png")
back_image = PhotoImage(file="images/back.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct_image = PhotoImage(file="images/right.png")

# Create a canvas to hold the flashcard images and text
canvas = Canvas(width=800, height=526)
flashcard_background = canvas.create_image(400, 263, image=front_image)
flashcard_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
flashcard_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg="#F5F5DC", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Set a timer to flip the flashcard after 4.5 seconds
card_view_time = window.after(4500, func=flip_flashcard)

# Create buttons for wrong and correct answers
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_flashcard)
wrong_button.grid(row=1, column=0)

correct_button = Button(
    image=correct_image, highlightthickness=0, command=correct_flashcard
)
correct_button.grid(row=1, column=1)

window.mainloop()
