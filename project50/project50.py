import os
import requests
import webbrowser
import sys
from datetime import datetime

def greet():
    print("Hello, I'm Project50, your virtual assistant! How can I assist you today?")

def get_weather():
    api = "9f2358a4637e058a3d95b06238572add"
    city = input("Enter city name: ")

    fullapilink = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    response = requests.get(fullapilink)
    data = response.json()
    if data["cod"] != "404":
        print("Invalid city name.")

        temperature = round(data["main"]["temp"] - 273.15, 2)
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        print(f"\nWeather Stats for {city.upper()} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("The temperature in", city, "is", temperature, "degrees Celsius.")
        print(f"Weather Description: {description}")
        print(f"Humidity: {humidity}%")

    else:
        print("Sorry, I couldn't find the weather for that city. \n")

def create_file():
    filename = input("Enter the name of the file: ")
    try:
        with open(filename, "w") as file:
            print("File created successfully :) \n")
    except:
        print("File could not be created, try again later :() \n")

def add_text_to_file():
    filename = input("Enter the name of the file: ")
    try:
        with open(filename, "a") as file:
            text = input("Enter the text to add: ")
            file.write(text + "\n")
        print("Text added to file successfully :) \n")
    except FileNotFoundError:
        print("Sorry, that file does'nt exist :( Would you like to create a new file")
        yes_no = input("Yes/No: ").lower
        if yes_no == "yes":
            create_file()
        elif yes_no == "no":
            sys.exit()
        else:
            print("Enter yes or no")
            print(yes_no)

def add_event_to_planner():
    date = input("Enter the date of the event (YYYY-MM-DD): ")
    time = input("Enter the time of the event (HH:MM): ")
    summary = input("Enter a summary of the event: ")
    description = input("Enter a description of the event: ")
    try:
        with open("planner.txt", "a") as file:
            file.write(f"Event: {summary}\n")
            file.write(f"Date: {date}\n")
            file.write(f"Time: {time}\n")
            file.write(f"Description: {description}\n")
            file.write("\n")
        print("Event added to planner successfully :) \n")
    except:
        print("Event could not be added to planner, try again later :(. \n")

def search_web():
    searchques = input("Enter a question: ")
    print(" ")
    googlesearch = "https://www.google.com/search?q=" + searchques
    webbrowser.open(googlesearch)

def main():
    greet()
    while True:
        print("I can get the weather")
        print("I can create a new file or add text to a file")
        print("I can add an event to your planner")
        print("I can surf the web")
        print("** To end the program type: exit ** \n")
        command = input("Enter a command to get started with Project50: ")

        if command == "exit":
            break
        elif "weather" in command:
            get_weather()
        elif "create file" in command:
            create_file()
        elif "add text" in command:
            add_text_to_file()
        elif "add event" in command:
            add_event_to_planner()
        elif "search" in command:
            search_web()
        else:
            print("Sorry, Project50 didn't understand that command, enter a valid command. \n")

if __name__ == "__main__":
    main()
