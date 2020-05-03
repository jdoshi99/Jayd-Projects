def flipcoin_func(NumberofHeads,NumberofTails):
	coinlist=['Heads','Tails']
	coinresult = random.choice(coinlist)
	if coinresult=='Heads':
		NumberofHeads+=1
	else:
		NumberofTails+=1
	return(NumberofHeads,NumberofTails)



if __name__ == '__main__':
	import random
	NumberofTails=0
	NumberofHeads=0
	userresponsetrue=True
	while userresponsetrue:
		userresponse= input(f'Would you like flip a coin? Enter Yes or No ')
		if userresponse.capitalize()=='Yes':
			NumberofHeads,NumberofTails=flipcoin_func(NumberofHeads,NumberofTails)
			print (f'Number of Heads= {NumberofHeads}')
			print (f'Number of Tails= {NumberofTails}')
			userresponsetrue=True
		elif userresponse.capitalize()=='No':
			print ('Goodbye')
			userresponsetrue=False
		else:
			print ('Please enter Yes or No')
			userresponsetrue=True