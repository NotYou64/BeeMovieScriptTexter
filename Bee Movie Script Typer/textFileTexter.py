# Cole Delong
# Script to send large text files (such as The Bee Movie) over text word by word
# 4/28/20

# imports
from pynput.keyboard import Key, Controller
import time

# main function
def main():

    # time to switch over to the Messenger app and rethink your life
    time.sleep(3)
    
    # setup
    keyboard = Controller()
    words = separateText(open("text.txt", "r").read())

    # type the words into the messenger app and hit return after every word. delay a tenth of a second per word
    for word in words:
        keyboard.type(word)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)

# function that takes a string as an input and returns a list of all the words in it
def separateText(text):

    # iterate through the sting adding all words to the array
    text = " " + text
    words = []
    lastSpace = 0
    for i in range(len(text)):
        if (text[i] == " " or i+1 == len(text)):
            word = text[lastSpace+1 : i+1]
            words.append(word)
            lastSpace = i            

    # return the array of words
    return words

# run main function
if __name__ == "__main__": main()

 
