    # PROJECT50 ASSISTANT
    #### Description:

    I initially struggled to come up with a project idea; I had been thinking about what to do
    for my final project since the beginning of the course. Throughout the course I had made multiple
    other projects an followed multiple other tutorials and learnt a lot outside CS50. YouTube channels
    like Free Code Camp and Tech With Tim helped with guidance - when talking about projects and games.
    I had created many smaller projects such as a weather fetcher and a simple planner program. I decided
    that for my project I wanted to compile all of those tool into one program and set it up to be an
    assistant program.

    Firstly, the greet function greets the user and introduces Project 50. Upon being greeted the user
    is given optioons of tasks that Project50 can complete and allows the user to choose. When certain
    keywords are entered by the user, the program excecutes specific functions. If invalid an error
    message is returned. The user is also prompted with an exit option to exit the program.

    Secondly, the weather function provides the user with the weather, it uses OpenWeatherAPI to gather
    information about the weather such as the temperature in degrees celcius, the humidity, and a
    description of the forecast. It asks theuser about the city they want the weather from and then
    provides them with the information. If the user entered an invalid city name the program returns an
    error message and, otehrwise the program returns another error message and reprompts the user to
    choose from the options again

    Thirdly, the create file function creates a new file. The user is prompted to enter a file name and the
    program then uses the 'open' and 'w' to create that new file. If created it returns a message saying so
    and if not the prgram returns a nerror message and repormpts the user to choose from the options again

    Next, an add text to file function allows the user t add text to an already existing file. This funciton
    prompts the user to enter the file name alongside the text they would like to add and if successful returns
    a message saying so. If not, an error messag eis returned and the user if asked whether or not they would
    like to create the file or not. If yes the program excecutes the, previously mentioned create file functions and if not the program exits.

    Then, the add event function adds events to a file called planner. If the file does not exist the program
    creates it and prmpts the user to enter the name, date, and time of the event. more events can be readded
    to this file, It's similar to the add text to file and the create new file function, but it adds text to
    one specifica file called planner.

    Afterwards, theres the search web function, this function allwos the user to ask the program something
    and the program then googles it and returns a search page. the program adds the google ur to the question
    and redirects user to the search page.

    Lastly, the main function combines everything. this is where the user is greeted and then Project50's
    task capabilities are listed for the user to choose from. by entering phrases comtaining certain
    keywords when prompted, the program returns certain functions that were described above. If an invalid
    command is entered the project prints out an error code and reprompts the user.

    In conclusion, Project50 is an assistant software. It provides user with seemingly simple taks, but it
    can be further developed and optimised. I would definelty like to learn a lot more and continue adding
    to it. Such as adding a GUI and more useful features to users.
