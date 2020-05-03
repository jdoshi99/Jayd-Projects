# Credit Card Validator

def checksum_func(creditcardlist):
	j=0
	creditcardtotalsum=0
	while j<(len(creditcardlist)-1):
		if j%2==0:
			creditcardlist[j]=creditcardlist[j]+creditcardlist[j]
			if creditcardlist[j]>9:
				creditcardlist[j]=creditcardlist[j]-10+1
			creditcardtotalsum+=creditcardlist[j]
			j+=1
		else:
			creditcardlist[j]=creditcardlist[j]
			creditcardtotalsum+=creditcardlist[j]
			j+=1
	creditcardtotalsum+=creditcardlist[15]
	if creditcardtotalsum%10==0:
		print('Valid Credit Card Number')
	else:
		print('Invalid Credit Card Number')
	
if __name__ == '__main__':
	cardvaluelist= {'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	creditcardlist=[]
	atleast16digits=True
	j=0
	while atleast16digits:
		creditcardnumbertocheck= input(f'Enter credit card number')
		creditcardstrlist=[]
		for i  in creditcardnumbertocheck:
			creditcardstrlist.append(i)
		if len(creditcardstrlist)!=16:
			print('Number needs to be 16 digit. Please Enter 16 digit credit card number')
			atleast16digits=True
		else:
			while j<len(creditcardstrlist):
				creditcardlist.append(int(creditcardstrlist[j]))
				j+=1

			checksum_func(creditcardlist)
			atleast16digits=False