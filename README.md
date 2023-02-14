# Icelandic-English Flashcard Application
## Overview
This is a simple GUI-based flashcard application that displays Icelandic words and their English translations. The program randomly selects words from a pre-defined list and displays them on a graphical flashcard. The user can flip the card to see the English translation and mark the card as correct or incorrect.

It lets the user learn the 1000 most used words in the Icelandic language (according to Open Subtitles, as obtained from https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Icelandic_wordlist).

## Requirements
To run this program, you will need Python 3 installed on your machine. You will also need the following Python libraries:
- pandas
- tkinter

## Installation
You can download the program files from this Github repository by clicking on the "Code" button and selecting "Download ZIP". Extract the files to a folder on your computer.

## Usage
To run the program, navigate to the folder where the program files are saved and open a terminal or command prompt. Run the following command:

`python main.py`

This will launch the program and the flashcards will start displaying automatically. Click the "Wrong" button if you don't know the answer, or click the "Correct" button if you do. The program will remove the current card from the list of cards to review, and save the updated list to a file.

## Customization
The program reads the list of words to display from a CSV file named "icelandic_words.csv" located in the "data" folder. You can modify this file to add or remove words from the flashcard list.

You can also modify the graphics used for the front and back of the flashcard by replacing the files "front.png" and "back.png" in the "images" folder.

## Contributing
This program is a simple demo project and is not currently accepting contributions.

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.
