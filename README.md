# Stonkers

### Grand Challenge

- Many people lack education when it comes to handle their own finances and investing money into the stock market
- Entry into the stock market can be intimidating especially for those who have a lot to lose
  - People won’t take the risk to lose real money in order to learn how to use the stock market
- Lots of jargon that can be intimidating to people who are not familiar with the stock market

### Proposed Solution

- Creating a game that gives a tutorial of how to navigate the stock market
- This game teaches you the basic stock trading, relevant terminology, and basic investment strategies
- Allows users to learn how to trade on the stock market without any risks–their real money is not on line

# Game Specs

- Screen Size: 1000 x 700

# Directory

- Media
  - Contains all media used in the game
- Code
  - Contains all python scripts that the game will run
- Files
  - Contains all non code files related to the project
- CSVFiles
  - Contains all CSV files that are related to the game

# Code

- Code/Gil's Code/Menu.py
    - Start Menu with animated button and background music
- AssetSelectionMenu.py
  - Will contain the code for the asset selection menu
- CurrentStocks.py
  - Gives you the current information for a stock that you select
- Player.py
  - Creates the player object
- Quiz.py
  - Will contain the code for the quiz that the players will play
- Stonkers.py
  - Game simulation file
- TradingGraph.py
  - Will contain the code for the trading graph
- TradingMenu.py
  - Will contain the code for the menu
- Educate.py
  - Teaches the player the jargon and skills they need to properly trade in the stock market

# Temporary Scripts

- window.py
  - Currently contains all of the front end
  - Needs to be broken up into its appropriate classes
- stonker.py
  - Currently contains all of the back end
  - Needs to be broke up into its appropriate classes

# Contributions

- Ponthea Zahraii
  - Created front end using pygames and matplotlib
    - Graphed historical stock data for TSLA
    - Created visuals for the main menu for the game
- Jason King
  - Planned how the classes were going to be organized
- Gilberto Arellano
  - Created the backlog
  - Created Menu, located in [Code/Gil's Code](https://github.com/jackmazac/stonker/tree/main/Code/Gil's%20Code)
- Daniel Boudigan
  - Created, in detail, the script for the educational aspects of the game
  - Finalized the storyboard and how the game should progress
- Jack Mazac
  - Created the backend of the game
    - Features include:
      - Buying
      - Selling
      - Login
      - Storing user data
      - Obtaining relevant stock information
- Jonathan Karam
  - Worked on editing the storyboard so the user is not overwhelmed with information

# Planned State vs. Current State

### Planned State

- Have graph visuals on screen
- Have interactive elements in the game
- Connect frontend and backend
- Have a very basic interactive game as a working prototype
- Multiple screens, each with different states
  - Home Screen
  - Educational Screen
  - Main Screen
  - End Screen

### Current State

- Graph with all the necessary data
  - Having difficulties adding the graph to the screen
- Clickable buttons that open and close drop down menus
- Working backend
- Educational materials have been decided–yet to be implemented

# Roadblocks

- Pygames is not a popular library that is used, therefore finding resources online to help us has been very limited
  - Has made simple debugging questions very time consuming
  - Unable to find a way to put a plot on the screen without the entire program crashing
- Learning curve with pandas
- Laziness and lack of communication within the team
- Different experience levels with coding/finance

# Plans for the future

### First Priority

Our first priority is to figure out how to add a matplotlib onto the screen

- We can use a picture of the graph instead of a graph
  - This would be a last ditch effort, I would not sugget this unless we have no other options
- We can search through the pygame documentation and test out the different methods that are listed
  - try all the methods that we searched through until we find one that works

### Goals

- Add interactive elements so the users can actually play the game
- Implement educational aspects of the game
- Possibly widen the availability of the program
  - Host website containing the game on github
- Potentially convert databases to a mySQL database so questioning and querying the data would be much simpler

### Tasks

- Add screens that teach users about the stock market
- Connect databases with the screens
- Allow for users to input and interact with the stock market data
- Add a testing feature to allow users to see how much they’ve learned by playing this game

# Sources

- https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
  - window.py
  - Used to create rectangles on the main window screen of the game
- https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
  - window.py
  - Used to create buttons to select stocks and bring drop down menu
- https://stackoverflow.com/questions/48093361/using-matplotlib-in-pygame
  - window.py
  - Used to figure out how to use matplotlib to plot TSLA data
- https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
  - window.py
  - Used to read info from the TSLA historical data CSV file to plot using matplotlib
- https://www.nasdaq.com/market-activity/stocks/tsla/historical
  - window.py
  - The historical TSLA stock dataset used in the game
- https://www.geeksforgeeks.org/how-to-rotate-and-scale-images-using-pygame/#:~:text=To%20scale%20the%20image%20we,manually%20according%20to%20our%20need.
  - window.py
  - Used to scale the background for the window
- https://www.w3schools.com/python/matplotlib_pyplot.asp
  - window.py
  - Further understand how matplotlib works to create plots
- https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
  - window.py
  - Used to read data from the CSV file to plot with matplotlib
- https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=4525s
  - Tutorial used to educate ourselves on how to use the pygame library
