def printboard():
	boardpattern = {'Line':'|', 'Underscore':'__', '1':'1','2':'2','3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
	print (boardpattern['1'], boardpattern['Line'], boardpattern['2'], boardpattern['Line'],boardpattern['3'])
	print (boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'])
	print (boardpattern['4'], boardpattern['Line'], boardpattern['5'], boardpattern['Line'],boardpattern['6'])
	print (boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'])
	print (boardpattern['7'], boardpattern['Line'], boardpattern['8'], boardpattern['Line'],boardpattern['9'])

def updateboardpattern(boardpattern, playerslotentry, player):
	boardpattern[playerslotentry]=player	
	print (boardpattern['1'], boardpattern['Line'], boardpattern['2'], boardpattern['Line'],boardpattern['3'])
	print (boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'])
	print (boardpattern['4'], boardpattern['Line'], boardpattern['5'], boardpattern['Line'],boardpattern['6'])
	print (boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'], boardpattern['Underscore'])
	print (boardpattern['7'], boardpattern['Line'], boardpattern['8'], boardpattern['Line'],boardpattern['9'])
	return(boardpattern)

def assignXorO():
	Player1=''
	Player2=''
	correctentry=True
	while correctentry:
		Player1 = input("Player 1- Would you like to be X or O? ")
		if Player1=='X' or Player1=='x':
			Player2='O'
			correctentry=False
		elif Player1=='O' or Player1=='o':
			Player2='X'
			correctentry=False
		else:
			print ("Please enter X or O")
			correctentry=True
	print (f"Player1 is  {Player1}")
	print (f"Player2 is  {Player2}")
	return(Player1, Player2)

def whogoesfirst():
	playerstartlist=[1,2]
	playerstart = random.choice(playerstartlist)
	if playerstart==1:
		print ("Player1 starts")
	else:
		print ("Player2 starts")
	return(playerstart)

def slotallocation(startingplayer,playerlist):
	updateboard = {'Line':'|', 'Underscore':'__', '1':' ','2':' ','3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
	availableslotlist=[' ', ' ',' ', ' ',' ', ' ',' ', ' ',' ',' ']
	Player1slotlist=[]
	Player2slotlist=[]
	num=0
	while num<9:
		slotisavailable=True
		if startingplayer==1:
			while slotisavailable:
				Player1slotentry= (input("Player1-Please select from positions 1-9 "))
				Player1slotentryint=int(Player1slotentry)
				if availableslotlist[Player1slotentryint]!=' ':
					print ("Slot is already taken. Enter another slot")
					slotisavailable=True
				else:
					availableslotlist[Player1slotentryint]=Player1slotentry
					Player1slotlist.append(Player1slotentry)
					updateboard=updateboardpattern(updateboard,Player1slotentry,playerlist[0])
					startingplayer=0
					num+=1
					slotisavailable=False
		else:
			while slotisavailable:
				Player2slotentry= (input("Player2-Please select from positions 1-9 "))
				Player2slotentryint=int(Player2slotentry)
				if availableslotlist[Player2slotentryint]!=' ':
					print ("Slot is already taken. Enter another slot")
					slotisavailable=True
				else:
					availableslotlist[Player2slotentryint]=Player2slotentry
					Player2slotlist.append(Player2slotentry)
					updateboard=updateboardpattern(updateboard,Player2slotentry,playerlist[1])
					startingplayer=1
					num+=1
					slotisavailable=False

	print (f" Player 1 Slots {Player1slotlist}")
	print (f" Player 2 Slots {Player2slotlist}")

if __name__ == '__main__':
	
	import random
	newgameloop=True
	playerlist={'Player1':' ', 'Player2':' '}
	while newgameloop:
		newgame = input("Would you like to play new game (Y/N)? ")
		if newgame =='Y' or newgame =='y':
			print ("Let's Play")
			newgameloop=True
			printboard()
			playerlist = assignXorO()
			startingplayer=whogoesfirst()
			slotallocation(startingplayer,playerlist)
		elif (newgame =='N' or newgame =='n'):
			print ("Goodbye")
			newgameloop=False
		else:
			print ("Please enter Y/N")
			newgameloop=True