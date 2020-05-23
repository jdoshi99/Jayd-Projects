#Function for Players to pick X or O
def playerpickXO_func():
	wrongentry=True
	p1pick=' '
	p2pick=' '
	while wrongentry:
		p1pick= input('Player 1. Would you like to be X or O? ')
		if p1pick.lower()=='x':
			p1pick='X'
			p2pick='O'
			wrongentry=False
		elif p1pick.lower()=='o':
			p1pick='O'
			p2pick='X'
			wrongentry=False
		else:
			print('Select X or O')
			wrongentry=True
	print("Player 1 is {}".format(p1pick))
	print("Player 2 is {}".format(p2pick))
	return p1pick,p2pick

def whogoesfirst_func():
	p1goes=0
	p2goes=0
	randomlist = [1,2]
	playergoesfirst = random.choice(randomlist)
	if playergoesfirst==1:
		p1goes=1
		p2goes=2
	else:
		p2goes=1
		p1goes=2
	print("Player 1 goes {}".format(p1goes))
	print("Player 2 goes {}".format(p2goes))
	return p1goes,p2goes

def printcurrentboard_func(brdnumber):
	boardpattern ={'A': ' ', 'B': '_', 'C': '|'}
	print(brdnumber['1'],boardpattern['C'],brdnumber['2'],boardpattern['C'],brdnumber['3'])
	print(boardpattern['B']*10)
	print(brdnumber['4'],boardpattern['C'],brdnumber['5'],boardpattern['C'],brdnumber['6'])
	print(boardpattern['B']*10)
	print(brdnumber['7'],boardpattern['C'],brdnumber['8'],boardpattern['C'],brdnumber['9'])

def slotavailable_func(pselslot,brdnumber):
	if brdnumber[pselslot]!= 'X' and brdnumber[pselslot]!= 'O':
		return True
	else:
		print('Slot is not available')
		return False

def checkforwin_func(board,mark):
	return ((board['7'] ==  board['8'] ==  board['9'] == mark) or # across the top \n,
    (board['4'] ==  board['5'] ==  board['6'] == mark) or # across the middle\n",
    (board['1'] ==  board['2'] ==  board['3'] == mark) or # across the bottom\n",
    (board['7'] ==  board['4'] ==  board['1'] == mark) or # down the middle\n",
    (board['8'] ==  board['5'] ==  board['2'] == mark) or # down the middle\n",
  	(board['9'] ==  board['6'] ==  board['3'] == mark) or # down the right side\n",
   	(board['7'] ==  board['5'] ==  board['3'] == mark) or # diagonal\n",
    (board['9'] ==  board['5'] ==  board['1'] == mark)) # diagonal"
    


def playandupdatebrd_func(brdnumber,p1goes,p2goes,p1pick,p2pick):
	#Function to ask players for position on board
	n=1
	player1slotlist =[]
	player2slotlist =[]
	while n<10:
		if p1goes==1:
			playerselslot= input ("Player 1. Select slot by entering numbers 1-9. ")
			#Function to check if slot is available
			slotisavailable= slotavailable_func(playerselslot,brdnumber)
			while slotisavailable:
				brdnumber[playerselslot]= p1pick
				printcurrentboard_func(brdnumber)
				#Update Player 1 slot list
				player1slotlist.append(int(playerselslot))
				#Check for Player1 Win after 3 moves by Player2
				winstatus=checkforwin_func(brdnumber,p1pick)
				if winstatus:
					print('Player 1 Wins')
					return()
				else:
					p1goes=0
					n+=1
					slotisavailable=False	
		else:
			playerselslot= input ("Player 2. Select slot by entering numbers 1-9. ")
			#Function to check if slot is available
			slotisavailable= slotavailable_func(playerselslot,brdnumber)
			while slotisavailable:
				brdnumber[playerselslot]= p2pick
				printcurrentboard_func(brdnumber)
				#Update Player 2 slot list
				player2slotlist.append(int(playerselslot))
					#Check for Player1 Win
				winstatus=checkforwin_func(brdnumber,p2pick)
				if winstatus:
					print('Player 2 Wins')
					return()
				else:
					p1goes=1
					n+=1
					slotisavailable=False
	print ('Draw Game')
	return()	

if __name__ == '__main__':
	import random
	
	#Loop to keep asking if Players want to play
	players_wanttoplay= True
	while players_wanttoplay:
	#Check if players want to play TicTacToe
		players_response = input('Would you like to play TicTacToe? Press Yes or No. ')
		if players_response.lower()=='yes' or players_response.lower()=='y':
			print('Lets get started')
			players_wanttoplay= True
			boardnumber ={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7, '8':8, '9':9}
			#Fuction Call for Players to pick X or O
			player1pick,player2pick = playerpickXO_func()
			#Function call to randomly select which player goes first
			player1goes,player2goes = whogoesfirst_func()

			#Function to print TicTacToeBoard
			printcurrentboard_func(boardnumber)
			#Fuction to ask player for slot and print updated board
			playandupdatebrd_func(boardnumber,player1goes,player2goes,player1pick,player2pick)

		else:
			print ('Good Bye')
			players_wanttoplay= False