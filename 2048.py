#2048 game codebase
#random module is imported for randomly generating 2's and 4's
import random 
#canContinue variable is used to depict that game can be continued
# (cells can be merged or there are cells with value 0)
CanContinue=1
#GameOver variable is set when game over condition is satisfied
# (either you win or lose)
GameOver=0

#generate a new game
def createGame():
    Board=list()
    for i in range (0,4):
        Board.append([0]*4)
    #generate twos in 2 cells, chosen randomly
    Board=generateRandomTwos(Board)
    return Board


#function to generate 2's in random cells
def generateRandomTwos(Board):
    #generate random row number
    randomRow=random.randint(0,3)
    #generate random column number 
    randomCol=random.randint(0,3)
    #as long as cell is not empty, keep generating random rows and columns 
    # till we can locate an empty cell
    while(Board[randomRow][randomCol]!=0):
        randomRow=random.randint(0,3)
        randomCol=random.randint(0,3)
    #place value 2 in empty cell
    Board[randomRow][randomCol]=2
    #repeat same step as above for placing the next 2 in a randomly selected cell
    while(Board[randomRow][randomCol]!=0):
        randomRow=random.randint(0,3)
        randomCol=random.randint(0,3)
    Board[randomRow][randomCol]=2
    return Board


#function to display the board
def display(Board):
    for i in range(4):
        for j in range(4):
            print(Board[i][j], end =" ")
        print()
    return Board


#function to check if game has ended or can still be played
def checkIfEndOfGameOrNot(Board):
    for i in range(0,4):
        for j in range(0,4):
            #if user obtains atleast one 2048 in one cell, user has won
            if(Board[i][j]==2048):
                return "You won"
    for i in range(4):
        for j in range(4):
            #if there is any cell with 0 in it, user can keep playing
            if(Board[i][j]==0):
                return "can keep playing"

    for i in range(3):
        for j in range(3):
            #if no cell is empty, but after either a down move or right move cells
            # can get merged, then also user can keep playing
            if(Board[i][j]== Board[i + 1][j] or Board[i][j]== Board[i][j + 1]):
                return "can keep playing"
 
    for j in range(3):
        #if last row's elements shifted to right can be merged, user can keep playing
        if(Board[3][j]== Board[3][j + 1]):
            return "can keep playing"
 
    for i in range(3):
        #if last column's elements shifted down can be merged, user can keep playing
        if(Board[i][3]== Board[i + 1][3]):
           return "can keep playing"
 
    # else user has lost the game
    return "Game over"      


#function to shift elements to left
def shiftleft(Board):
    Boardcopy = []
    for i in range(0,4):
        Boardcopy.append([0]*4)
    #for every non empty cell, shift the element to the same row's left most cells
    for i in range(0,4):
          pos=0
          for j in range(0,4):
              if(Board[i][j]!=0):
                  Boardcopy[i][pos]=Board[i][j]
                  pos+=1
    return Boardcopy


#function to merge cells if adjacent cells have same value
def mergeCells(Board):
    for i in range(0,4):
        for j in range(0,3):
            #if cell is not empty and cell's adjacent neighbour has same value, double 
            # cell's value, adjacent neighbour's value should be made 0(depicts empty cell)
            if(Board[i][j]!=0 and Board[i][j]==Board[i][j+1]):
                Board[i][j]=Board[i][j]*2
                Board[i][j+1]=0
    return Board


#function to reverse elements in a row, for shifting right
def reverse(Board):
    newBoard=[]
    for i in range(0,4):
        newBoard.append([])
        for j in range(0,4):
            newBoard[i].append(Board[i][3-j])
    return newBoard


#function to return transpose of the board
def transpose(Board):
    newBoard=[]
    for i in range(0,4):
        newBoard.append([0]*4)
    for i in range(0,4):
        for j in range(0,4):
            newBoard[i][j]=Board[j][i]
    return newBoard


#function to generate random numbered tiles(either 2 or 4), in a random empty cell
def addnewtile(Board):
    randomRow=random.randint(0,3)
    randomCol=random.randint(0,3)
    while(Board[randomRow][randomCol]!=0):
        randomRow=random.randint(0,3)
        randomCol=random.randint(0,3)
    Board[randomRow][randomCol]=random.choice([2,4])
    return Board

#function to move tiles to left, when user presses 1
#shift elements to left, merge cells if there are adjacent cells with same values
#add new tile with 2 or 4 randomly generated, display the board after the previous moves
#check if we have reached end of the game,if game is over(You lost or won), 
#print it and GameOver variable is set, canContinue is reset
def leftmove(Board):
    Board=shiftleft(Board)
    Board=mergeCells(Board)
    Board=shiftleft(Board)
    Board=addnewtile(Board)
    Board=display(Board)
    status=checkIfEndOfGameOrNot(Board)
    if(status=="You won" or status=="Game over"):
        if(status=="Game over"):
           print("You lost")
        else:
           print("You won")
        GameOver=1
        CanContinue=0
    else:
        CanContinue=1
    return Board
    
#function to move right when user presses 2 
# reverse the Board and proceed as in leftmove function
# then reverse the Board again to get the result after right move
# add new tile , display board, check if end of game is reached
# if so, print it and GameOver variable is set, canContinue is reset   
def rightmove(Board):
    Board=reverse(Board)
    Board=shiftleft(Board)
    Board=mergeCells(Board)
    Board=shiftleft(Board)
    Board=reverse(Board)
    Board=addnewtile(Board)
    Board=display(Board)
    status=checkIfEndOfGameOrNot(Board)
    if(status=="You won" or status=="Game over"):
        if(status=="Game over"):
           print("You lost")
        else:
           print("You won")
        GameOver=1
        CanContinue=0
    else:
        CanContinue=1
    return Board

#function to move up when user presses 3
#transpose the matrix, perform shiftleft
#merge the cells and again perform shiftleft
#find transpose of the matrix and return it
#add new tile , display board, check if end of game is reached
# if so, print it and GameOver variable is set, canContinue is reset   
def upmove(Board):
    Board=transpose(Board)
    Board=shiftleft(Board)
    Board=mergeCells(Board)
    Board=shiftleft(Board)
    Board=transpose(Board)
    Board=addnewtile(Board)
    Board=display(Board)
    status=checkIfEndOfGameOrNot(Board)
    if(status=="You won" or status=="Game over"):
        if(status=="Game over"):
           print("You lost")
        else:
           print("You won")
        GameOver=1
        CanContinue=0
    else:
        CanContinue=1
    return Board

#function to move down when user presses 4
#transpose the matrix, perform reverse
#merge the cells and perform shiftleft
#find reverse of the matrix, and then transpose and return it
#add new tile , display board, check if end of game is reached
#if so, print it and GameOver variable is set, canContinue is reset 
def downmove(Board):
    Board=transpose(Board)
    Board=reverse(Board)
    Board=shiftleft(Board)
    Board=mergeCells(Board)
    Board=shiftleft(Board)
    Board=reverse(Board)
    Board=transpose(Board)
    Board=addnewtile(Board)
    Board=display(Board)
    status=checkIfEndOfGameOrNot(Board)
    if(status=="You won" or status=="Game over"):
        if(status=="Game over"):
           print("You lost")
        else:
           print("You won")
        GameOver=1
        CanContinue=0
    else:
        CanContinue=1
    return Board

#main function
if __name__ == '__main__':
    #call createGame function to create new game
    Board=createGame()
    Board=display(Board)
    while(True):
        print("Enter command")
        print("Commands are as follows : ")
        print("1 : Move Left")
        print("2 : Move Right")
        print("3 : Move Up")
        print("4 : Move Down")
        print("5: exit")
        key=int(input())
        if(key==1):
           if(CanContinue):
              Board=leftmove(Board)
           else:
                exit(0)
        elif(key==2):
           if(CanContinue):
              Board=rightmove(Board)
           else:
                exit(0)
        elif(key==3):
           if(CanContinue):
              Board=upmove(Board)
           else:
                exit(0)
        elif(key==4):
           if(CanContinue):
              Board=downmove(Board)
           else:
                exit(0)
        elif(key==5):
           exit(0)
        else:
           print("Invalid option")
    


