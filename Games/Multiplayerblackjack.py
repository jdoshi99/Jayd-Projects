#Player Class to store Player information
class Playersclass:
	def __init__(self, name, balance,cards,cardsvalue,betamount):
		self.name = name
		self.balance = balance
		self.cards = cards
		self.cardsvalue = cardsvalue
		self.betamount = betamount

	def playerinfo_func(self):
		print('Player Name is {} and his balance is {}'.format(self.name,self.balance))

	def playercardinfo_func(self):
		print('{} cards are {}'.format(self.name,self.cards))
		print('{} cardsvalue is {}'.format(self.name,self.cardsvalue))

	def betamtandbalancecheck_func(self):
		print('{} balance is {}'.format(self.name, self.balance))
		validbetamount=True
		while validbetamount:
			self.betamount = int(input('{} enter your bet amount '.format(self.name)))
			if (self.betamount<self.balance or self.betamount==self.balance):
				self.balance = self.balance-self.betamount
				validbetamount=False
			else:
				print('Not Enough Balance. Your balance is {}. Enter another bet amount'.format(self.balance))
				validbetamount=True


#Dealer Class to store Player information
class Dealerclass:
	def __init__(self,cards,cardsvalue):
		self.cards=cards
		self.cardsvalue=cardsvalue

	def dealercardinfo_func(self,firsttime):
		if firsttime:
			print('Dealer cards are {}'.format(self.cards[0]))
						
		else:
			print('Dealer cards are {}'.format(self.cards))
			print('Dealer cardsvalue is {}'.format(self.cardsvalue))

def getplayerinfo_func(Players,numofplayers):

	#Loop to get player information
	for i in range(0,numofplayers):
		Players[i].name = input('Enter Players Name. ')
		Players[i].balance = int(input('Enter Player balance in $. '))
		Players[i].playerinfo_func()


def dealcards_func():
	cardtypelist = ['Diamond','Spade','Heart','Club']
	cardnumberlist = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
	
	pickcardtype = random.choice(cardtypelist)
	pickcardnumber = random.choice(cardnumberlist)
	pickcard=pickcardnumber +'of'+pickcardtype
	return pickcard,pickcardnumber

def playerhit_func(Players,numofplayers):
	for l in range(0,numofplayers):
		hit=True
		oneoreleven=False
		oneshot=True
		while hit:
			hitresponse = (input('{} would you like to hit? '.format(Players[l].name)))
			if hitresponse.lower()=='yes':
				cardtype,cardnumber = dealcards_func()
				Players[l].cards.append(cardtype)
				Players[l].cardsvalue+=cardvaluedict[cardnumber]
				oneoreleven=aceoneoreleven_func(Players[l].cardsvalue,Players[l].cards)
				if oneoreleven and oneshot:
					Players[l].cardsvalue=Players[l].cardsvalue-10
					Players[l].playercardinfo_func()
					oneshot=False
				else:
					Players[l].playercardinfo_func()
					bustorblack=bustorblackjack_func(Players[l].cardsvalue)
					if bustorblack==0:
						hit=True
					elif bustorblack==1:
						print('{} cards are {}. Player is busted'.format(Players[l].name,Players[l].cards))
						hit=False
					else:
						print('{} cards are {}. Player has blackjack'.format(Players[l].name,Players[l].cards))
						hit=False

			elif  hitresponse.lower()=='no':
				Players[l].playercardinfo_func()
				hit=False
			else:
				print('Enter Yes or No.')
				hit=True

def dealerhit_func(Dealer):
	lessthan17=True
	oneoreleven=False
	oneshot=True
	while lessthan17:
		if Dealer.cardsvalue<17:
			cardtype,cardnumber = dealcards_func()
			Dealer.cards.append(cardtype)
			Dealer.cardsvalue+=cardvaluedict[cardnumber]
			oneoreleven=aceoneoreleven_func(Dealer.cardsvalue,Dealer.cards)
			if oneoreleven and oneshot:
				firstgo=False
				Dealer.cardsvalue=Dealer.cardsvalue-10
				Dealer.dealercardinfo_func(firstgo)
				oneshot=False
			else:
				firstgo=False
				Dealer.dealercardinfo_func(firstgo)
				bustorblack=bustorblackjack_func(Dealer.cardsvalue)
				if bustorblack==0:
					lessthan17=True
				elif bustorblack==1:
					print('Dealer cards are {}. Dealer is busted'.format(Dealer.cards))
					lessthan17=False
				else:
					print('Dealer cards are {}. Dealer has blackjack'.format(Dealer.cards))
					lessthan17=False
		else:
			firstgo=False
			Dealer.dealercardinfo_func(firstgo)
			bustorblack=bustorblackjack_func(Dealer.cardsvalue)
			if bustorblack==1:
				print('Dealer cards are {}. Dealer is busted'.format(Dealer.cards))
				lessthan17=False
			elif bustorblack==2:
				print('Dealer cards are {}. Dealer has blackjack'.format(Dealer.cards))
				lessthan17=False
			lessthan17=False


def aceoneoreleven_func(cardsvalue,cards):
	for i in range(0,len(cards)):
		print(cards[i])
		print(cardsvalue)
		if (cards[i]=='AceofHearts' or cards[i]=='AceofDiamond' or cards[i]=='AceofSpade' or cards[i]=='AceofClub'  and cardsvalue>21):
			return True


def bustorblackjack_func(cardsvalue):
	#bustoroblackjack=0 means contineu, bustorblackjack=1 means busted, bustorblackjack=2 means blackjack
	bustorblack=0
	if cardsvalue>21:
		bustorblack=1
		return bustorblack
	elif cardsvalue==21:
		bustorblack=2
		return bustorblack
	else:
		return bustorblack

def checkforwin_func(Players, numofplayers,Dealer):
	for i in range(0,numofplayers):
		if ((Players[i].cardsvalue==Dealer.cardsvalue) and (Players[i].cardsvalue<22)) :
			print('{} is tied with the Dealer'.format(Players[i].name))
			Players[i].balance+=Players[i].betamount
			print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
		if (Players[i].cardsvalue<Dealer.cardsvalue) and (Dealer.cardsvalue<21):
			print('{} lost'.format(Players[i].name))
			print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
		if (Players[i].cardsvalue>Dealer.cardsvalue) and (Players[i].cardsvalue<22) and (Dealer.cardsvalue<21):
			print('{} wins'.format(Players[i].name))
			Players[i].balance=Players[i].balance+Players[i].betamount+Players[i].betamount
			print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
		if (Players[i].cardsvalue<22) and (Dealer.cardsvalue>21):
			print('{} wins'.format(Players[i].name))
			Players[i].balance=Players[i].balance+Players[i].betamount+Players[i].betamount
			print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
		if (Players[i].cardsvalue>21) and (Dealer.cardsvalue<21):
			print('{} lost'.format(Players[i].name))
			print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
		if (Dealer.cardsvalue==21):
			if (Players[i].cardsvalue):
				print('{} is tied with the Dealer'.format(Players[i].name))
				Players[i].balance+=Players[i].betamount
			else:
				print('{} lost'.format(Players[i].name))
				print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
		if (Players[i].cardsvalue>21) and (Dealer.cardsvalue>21):
			Players[i].balance=Players[i].balance+Players[i].betamount
			print('{} new balance is {}'.format(Players[i].name,Players[i].balance))
			
if __name__ == '__main__':
	import random
	#Ask if players want to play Blackjack
	wanttoplayblackjack=True
	name=''
	balance=0
	cards=[]
	cardsvalue=0
	betamount=0
	
	cardvaluedict = {'Ace':11,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
	while wanttoplayblackjack:
		playblackjackresponse= input('Would you like to play Black Jack. Enter Yes or No? ')
		wanttoplayblackjack=True
		if playblackjackresponse.lower()=='yes' or playblackjackresponse.lower()=='y':
			sameplayers=True
			while sameplayers:
				sameplayersresponse = input('Same Players or New Players? Enter Same or New. ')
				if sameplayersresponse.lower()=='new':

					#Function to get player name and balance
					numberofplayers= int(input('Enter number of players '))
					Dealer = Dealerclass(cards,cardsvalue)
					Players = [Playersclass(name,balance,cards,cardsvalue,betamount) for i in range(numberofplayers)]
					getplayerinfo_func(Players,numberofplayers)
					sameplayers=False

				elif sameplayersresponse.lower()=='same':
					sameplayers=False

				else:
					sameplayers=True
					print ('Enter Same or New')

			#Get bet amounts
			for i in range(0,numberofplayers):
				Players[i].betamtandbalancecheck_func()

			#Function to deal cards and print players card and determine cardsvalue
			for k in range(0,numberofplayers):
				Players[k].cards=[]
				totcardvalue=0
				for j in range(0,2):
					cardtype,cardnumber = dealcards_func()
					totcardvalue+=cardvaluedict[cardnumber] 
					Players[k].cards.append(cardtype)
					Players[k].cardsvalue = totcardvalue
				Players[k].playercardinfo_func()
				

			#Function to deal cards and print players card and determine cardsvalue
			totcardvalue=0
			Dealer.cards=[]
			for j in range(0,2):				
				cardtype,cardnumber = dealcards_func()
				totcardvalue+=cardvaluedict[cardnumber]
				Dealer.cards.append(cardtype)
				Dealer.cardsvalue = totcardvalue
			firstgo=True
			Dealer.dealercardinfo_func(firstgo)

			#Function to check if player would like to hit and update player card and cardvale
			playerhit_func(Players,numberofplayers)
			dealerhit_func(Dealer)
			checkforwin_func(Players,numberofplayers,Dealer)

			
		elif playblackjackresponse.lower()=='no' or playblackjackresponse.lower()=='n':
			print('Goodbye')
			wanttoplayblackjack=False
		else:
			wanttoplayblackjack=True
			print ('Enter Yes or No')