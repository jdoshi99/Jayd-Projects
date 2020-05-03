#Player Class to store Player information
class Playersclass:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def playerinfo_func():
		print(self.name)
		print(self.balance)


if __name__ == '__main__':
	#Ask if players want to play Blackjack
	wanttoplayblackjack=True
	while wanttoplayblackjack:
		playblackjackresponse= input('Would you like to play Black Jack. Enter Yes or No? ')
		if playblackjackresponse.lower()=='yes' or playblackjackresponse.lower()=='y':
			wanttoplayblackjack=True
			numofplayers= int(input('Enter number of players'))
			Players = [Playersclass() for i in range(numofplayers)]
			#Loop to get player information
			for i in range(0,numofplayers):
				Players[i].name = input('Enter Players Name. ')
				Players[i].balance = input('Enter Player balance in $. ')
			
		elif playblackjackresponse.lower()=='no' or playblackjackresponse.lower()=='n':
			print('Goodbye')
			wanttoplayblackjack=False
		else:
			wanttoplayblackjack=True
			print ('Enter Yes or No')