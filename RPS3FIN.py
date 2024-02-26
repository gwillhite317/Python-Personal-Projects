#Greyson Willhite
#Rock Paper Scissors Game with some colors for fun!

import random
from graphics import *

rock = 1
paper = 2
scissors = 3   #assign each option to a value 1-3

playerWins = 0
computerWins = 0
ties = 0    #set the default values to zero

def computerPicks():
    return random.randint(1,3)    #here we get the computers pick

def getWinner(playerPicks, computerPicks):    #we use the computers pick as a paramater and another parameter to represent user input
    global playerWins, computerWins, ties
    if playerPicks == computerPicks:
        ties += 1   #This is the one scenario in which a tie will happen
        return "Tie"
    elif playerPicks == rock and computerPicks == scissors or \
         playerPicks == paper and computerPicks == rock or \
         playerPicks == scissors and computerPicks == paper:
        playerWins += 1
        return "You win"   #here we establish all scenarios where the user wins
    else:
        computerWins += 1
        return "Computer Wins"    #because the user wins for the scenarios above we can assume the computer wins for all other scnarios

win = GraphWin("Rock-Paper-Scissors", 300,300)   #create the window and set the color to cyan for fun
win.setBackground("cyan")

rock_button = Rectangle(Point(50,50), Point(125, 125))      #create the rock button, all buttons are equally spread out on the grid according to the window size
rock_button.setFill("red")
rock_text = Text(Point(87,87), "Rock")
rock_button.draw(win)
rock_text.draw(win)

paper_button = Rectangle(Point(175, 50), Point(250, 125))     #creating the paper button
paper_button.setFill("purple")
paper_text = Text(Point(212, 87), "Paper")
paper_button.draw(win)
paper_text.draw(win)

scissors_button = Rectangle(Point(50, 150), Point(125, 225))   #creating the scissors button
scissors_button.setFill("yellow")
scissors_text = Text(Point(87, 187), "Scissors")
scissors_button.draw(win)
scissors_text.draw(win)

quit_button = Rectangle(Point(175, 150), Point(250, 225))    #creating the quit button
quit_button.setFill("green")
quit_text = Text(Point(212, 187), "Quit")
quit_button.draw(win)
quit_text.draw(win)

playerPickText = Text(Point(75, 135), "")       #I had to declare these two outside of the while loop because they were-
computerPickText = Text(Point(225, 135), "")   #overlapping, this way the string gets updated inside of the loop

while True: #This is where we get our input, the values are based off of the locations of the buttons within the window
    player_clicks = win.getMouse()
    if player_clicks.getX() >= 50 and player_clicks.getX() <= 125 and \
            player_clicks.getY() >= 50 and player_clicks.getY() <= 125:
        playerPicks = rock
    elif player_clicks.getX() >= 175 and player_clicks.getX() <= 250 and \
            player_clicks.getY() >= 50 and player_clicks.getY() <= 125:
        playerPicks = paper
    elif player_clicks.getX() >= 50 and player_clicks.getX() <= 125 and \
            player_clicks.getY() >= 150 and player_clicks.getY() <= 225:
        playerPicks = scissors
    elif player_clicks.getX() >= 175 and player_clicks.getX() <= 250 and \
            player_clicks.getY() >= 150 and player_clicks.getY() <= 225:
        break
    else:
        continue

    computerPick = computerPicks()

    resultMessage = getWinner(playerPicks, computerPick)#here we make the result message, we define the parameters below
    if "result_text" in locals():
        result_text.undraw()    #using undraw I wipe out the old message so there is no overlapping
    result_text = Text(Point(150, 255), resultMessage)
    result_text.draw(win)

    scoreboardMessage = f"Player: {playerWins} | Computer: {computerWins} | Ties: {ties}"  #makes scoreboard at the top
    if "scoreboardText" in locals():
        scoreboardText.undraw()
    scoreboardText = Text(Point(150, 25), scoreboardMessage)
    scoreboardText.draw(win)

    if playerPicks == rock:
        playerPickText.setText("User : Rock")   #here is where we equate the results from our while function into a string
    elif playerPicks == paper:
        playerPickText.setText("User : Paper")
    elif playerPicks == scissors:
        playerPickText.setText("User : Scissors")

    if computerPick == rock:
        computerPickText.setText("Computer : Rock")     #doing the same thing for the computers random pick
    elif computerPick == paper:
        computerPickText.setText("Computer : Paper")
    elif computerPick == scissors:
        computerPickText.setText("Computer : Scissors")

    if "playerPickText" in locals():    #Here we clear the previous player pick and draw the new one
        playerPickText.undraw()
    playerPickText.draw(win)

    if "computerPickText" in locals():    #doing the same for the computers pick
        computerPickText.undraw()
    computerPickText.draw(win)

    quitMessage =  "Click Quit to exit"  #lastly I displayed a quit message at the bottom of the screen
    if "quit_txt" in locals():
        quit_txt.undraw()
    quit_txt = Text(Point(150, 280), quitMessage)
    quit_txt.draw(win)
