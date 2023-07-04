# https://www.youtube.com/watch?v=Oz3W-LKfafE (automation projects)

import sys
import clipboard
import json

SAVED_DATA = "clipbard.json"

# how to use clipboard module:
# data = clipboard.paste()
# print(data) , prints whats on clipboard
# cipboard.copy("abc")
# run code and then paste

# print(sys.argv)
# print(sys.argv[1:]) remove the first word from the passed command

def save_items(filepath, data):
    with open(filepath, "w") as f:
    # write a file and f means store whatever written
        json.dump(data, f)
        # write the data as a json file nd dump the data

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            # will read the file and give python representation in form of dictionary of the file
            return data
    except:
        return{}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":

        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("Data saved successfully!")

        # ask for key then store the key associated with whats in clipboard then call save data to save
        # will get eror if the file doesnt exist

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key does not exist")
        # asked to enter key, check if the key exists and copy to clipboard, else print doesnt exist

    elif command == "list":
        print(data)
    else:
        print("Unknown command")

else:
    print("Pass exactly one command")
