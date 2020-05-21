# class TicTacToe():
""" This is the well-known game of Tic-Tac-Toe. Players X and Y 
take turns choosing a square on the board until one player 
scores three in a row. """
def gameBoard(currentlst):
	# A new game will start with blank inputs. Every time a user input is added to currentlst, this function will be re-run to update and print the board.
	row_label = [" ", " ", " ", "1", " ", "2", " ", "3"]
	row_sepa = [" ", " ", " ", "_", "_", "_", "_", "_"]
	row_sepb = [" ", " ", " ", " ", " ", " ", " ", " "]
	rowa = ["1", "|", " ", " ", "|", " ", "|", " "]
	rowlina = [" ", "|", " ", "-", "-", "-", "-", "-"]
	rowb = ["2", "|", " ", " ", "|", " ", "|", " "]
	rowlinb = [" ", "|", " ", "-", "-", "-", "-", "-"]
	rowc = ["3", "|", " ", " ", "|", " ", "|", " "]

	for i in range(0,3):
		for j in range(0, 3):
			if currentlst[i][j] != "":
				if i == 0:
					if j == 0:
						rowa[j+3] = currentlst[i][j]
					elif j == 1:
						rowa[j+4] = currentlst[i][j]
					elif j == 2:
						rowa[j+5] = currentlst[i][j]
				elif i == 1:
					if j == 0:
						rowb[j+3] = currentlst[i][j]
					elif j == 1:
						rowb[j+4] = currentlst[i][j]
					elif j == 2:
						rowb[j+5] = currentlst[i][j]
				elif i == 2:
					if j == 0:
						rowc[j+3] = currentlst[i][j]
					elif j == 1:
						rowc[j+4] = currentlst[i][j]
					elif j == 2:
						rowc[j+5] = currentlst[i][j]
	currentBoard = []
	currentBoard.append(row_label) 
	currentBoard.append(row_sepa)
	currentBoard.append(row_sepb) 
	currentBoard.append(rowa) 
	currentBoard.append(rowlina)
	currentBoard.append(rowb)
	currentBoard.append(rowlinb)
	currentBoard.append(rowc)
	return currentBoard

def isWin(currentlst):
	#There are 8 WIN conditions. There are 3 rows, 3 columns, and 2 diagonals. Check each for 3 equal chars and return True if there is a match
	victory = False
	player = ""
	if (currentlst[0][0] == currentlst[1][0] == currentlst[2][0]) and currentlst[0][0] != '':   #First Column
		victory = True
		player += currentlst[0][0]
	if (currentlst[0][1] == currentlst[1][1] == currentlst[2][1]) and currentlst[0][1] != '':   #Second Column
		victory = True
		player += currentlst[0][1]
	if (currentlst[0][2] == currentlst[1][2] == currentlst[2][2]) and currentlst[0][2] != '':   #Third Column
		victory = True
		player += currentlst[0][2]
	if (currentlst[0][0] == currentlst[0][1] == currentlst[0][2]) and currentlst[0][0] != '':   #First Row
		victory = True
		player += currentlst[0][0]
	if (currentlst[1][0] == currentlst[1][1] == currentlst[1][2]) and currentlst[1][0] != '':   #Second Row
		victory = True
		player += currentlst[1][0]
	if (currentlst[2][0] == currentlst[2][1] == currentlst[2][2]) and currentlst[2][0] != '':   #Third Row
		victory = True
		player += currentlst[2][0]
	if (currentlst[0][0] == currentlst[1][1] == currentlst[2][2]) and currentlst[0][0] != '':   #Diagonal TL to BR
		victory = True
		player += currentlst[0][0]
	if (currentlst[0][2] == currentlst[1][1] == currentlst[2][0]) and currentlst[0][2] != '':   #Diagonal TR to BL
		victory = True
		player += currentlst[0][2]
	if victory == True:
		print("Congratulations! Player '%s' has won the game!!" %(player))
		return victory

def main():
	currentlst = [["","",""],["","",""],["","",""]]
	victory = False
	x_turn = 0 # counts number of turns to ensure players alternate
	y_turn = 0
	while not victory: #iterate until one player achieves the victory condition
		if x_turn == 5:
			currentBoard = gameBoard(currentlst)  #print out current board
			for s in currentBoard:
				print(*s)
			print("You have reached a draw! Thanks for playing.")
			break
		if x_turn == y_turn:
			x_good = False
			while not x_good:
				try:  #take players input, repeating if the player fails to input a valid selection
					currentBoard = gameBoard(currentlst)  #print out current board
					for s in currentBoard:
						print(*s)
					x_row = int(input("Player X --> Choose a row: "))
					x_col = int(input("Player X --> Choose a column: "))
					if currentlst[x_row-1][x_col-1] == "":  #checks that the square isn't already taken
						currentlst[x_row-1][x_col-1] = "X"
						x_good = True  #mark that the turn is valid
						victory = isWin(currentlst)  #recheck the victory condition
						x_turn +=1  #iterate player X's turn
					else:
						print()
						print("That square is already taken. Try again.")
				except ValueError:
					print("You did not enter a positive integer between 1 and 3. Try again")
		elif y_turn < x_turn:
			y_good = False
			while not y_good:
				try:
					currentBoard = gameBoard(currentlst)
					for s in currentBoard:
						print(*s)
					y_row = int(input("Player Y --> Choose a row: "))
					y_col = int(input("Player Y --> Choose a column: "))
					if currentlst[y_row-1][y_col-1] == "":
						currentlst[y_row-1][y_col-1] = "Y"
						y_good = True
						victory = isWin(currentlst)
						y_turn +=1
					else:
						print()
						print("That square is already taken. Try again.")
				except ValueError:
					print("You did not enter a positive integer between 1 and 3. Try again")

if __name__ == "__main__":
	main()