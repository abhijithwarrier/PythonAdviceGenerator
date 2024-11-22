# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GENERATE ADVICE BY MAKING API CALLS TO Advice Slip JSON API
#
# The Advice Slip JSON API is provided for free. It currently gives out over 10 million pieces of advice every year.
#
# MORE INFO AVAILABLE AT - https://api.adviceslip.com/#top

# Importing necessary packages
import base64
import json
import requests
import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    adviceLabel = Label(root, text="ADVICE : ", bg="deepskyblue4", font=('Comic Sans MS',15,'bold'))
    adviceLabel.grid(row=1, column=0, padx=10, pady=5)

    root.adviceText = sb_text.ScrolledText(root, width=30, height=5, bg='azure3')
    root.adviceText.grid(row=3, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.adviceText.config(state=DISABLED, font = "Calibri 15", wrap="word")

    getAdviceButton = Button(root, text="GET ADVICE", command=getAdvice)
    getAdviceButton.grid(row=9, column=0, padx=10, pady=5, columnspan=3)

# Defining the getAdvice() to generate and display advice
def getAdvice():
    # Sending request to the Advice Slip JSON API endpoint
    advice_output = requests.get('https://api.adviceslip.com/advice')
    # Converting the response to the json
    advice_output_json = json.loads(advice_output.text)
    print(advice_output_json)
    # Fetching the advice from the above json output
    advice_result = advice_output_json['slip']['advice']
    print(advice_result.encode('utf-8').hex())
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.adviceText.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.adviceText.delete('1.0', END)
    # Displaying the generated advice in the adviceText Widget
    root.adviceText.insert("end", advice_result)
    # Making Widget uneditable again after the displaying quote of the day
    root.adviceText.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("PythonAdviceGenerator")
root.geometry("345x200")
root.config(background="deepskyblue4")
root.resizable(False, False)
# Creating the tkinter variables
song = StringVar()
artist = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
