# Import the necessary libraries
from tkinter import *
import pandas as pd
import random


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

# Create buttons for wrong and correct answers
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_flashcard)
wrong_button.grid(row=1, column=0)

correct_button = Button(
    image=correct_image, highlightthickness=0, command=correct_flashcard
)
correct_button.grid(row=1, column=1)

window.mainloop()
