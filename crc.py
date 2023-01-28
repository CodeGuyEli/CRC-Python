#! /usr/bin/python3

import sys
import json
RespondDict = {}
def save(filename):
    out_file = open(filename, "w")
    json.dump(RespondDict, out_file, indent = 6)
	
    out_file.close()
def load(filename):
    with open(filename) as f_in:
        RespondDict = json.load(f_in)
def start():
    print("Do you have a saved data file? Type yes or no")
    respond = input("")
    if respond.lower.startswith(y):
        file = input("Enter the filename:")
        load(file)
def train():
    global say
    respond = input("I didn't understand. What should I say next time?")
    RespondDict[say] = respond
def ask():
    global say
    say = input("What would you like to say?")
    if say == "Bye!":
        check = input("Would you like to save? y or n?")
        if check == "y":
            file = input("Name?")
            save(file)
        print("Bye!")
        sys.exit()
    if say in RespondDict.keys():
        print(RespondDict[say])
    else:
        train()
while True:
    ask()
