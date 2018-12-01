#start
import os
#Functions
def add(x,y):
#function for addition	
	return x+y

def sub(x,y):#function for substraction
	return x-y

def mul(x,y):#function for multiplication
	return x*y

def div(x,y):
#function for division
	return x/y

def exp(x,y):#function for exponential
	return x**y

def mod(x,y):#function for modulus operator
	return x%y


ch=('y')#condition variable
while ch not in ('n','NO','no','N'):
	print "\t MENU\n\t1.ADDITION\n\t2.SUBSTRACTION\n\t3.MULTIPLICATION\n\t4.DIVISION\n\t5.EXPONENTIAL\n\t6.REMAINDER"
 #printing the menu
	n=input("ENTER CHOICE")
	if (n>0 and n<7):

		a=input("ENTER FIRST NUMBER:")

		b=input("ENTER SECOND NUMBER:")
	
		print "\tTHE ANSWER IS ",
	
		if(n==1):
		
			print add(a,b)

		elif(n==2):
		
			print sub(a,b)

		elif(n==3):
		
			print mul(a,b)

		elif(n==4):
		
			print div(a,b)
	
		elif(n==5):
		
			print exp(a,b)
	
		elif(n==6):
		
			print mod(a,b)
	
		else:
			print "INVALID CHOICE"
		c=raw_input("Do you wish to do more calculations :")
		ch=c
		os.system("cls")
print("Thank you")
#end
