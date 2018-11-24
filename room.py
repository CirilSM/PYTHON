ernakulam={"Holiday Inn":4500,"Marriot":3000,"Crown Plaza":3000}
kozhikode={"Raviz":7000,"The Taj":6000,"Kadavu":5500}
thrissur={"Joys Palace":4500,"Lulu Convention Centre":5000,"Dass Continental":2500}
#all the hotels
print("\t\t\t\tChoose District\n\t\t\t\t1.Ernakulam\n\t\t\t\t2.Kozhikode\n\t\t\t\t3.Thrissur\n\n")#printing the menu for districts
ch=input("Enter the Choice")
pr=0
rooms=0
n=""
u=""
type=""
t=1
while(t==1):
	if(ch==1):
		print("\n\t\t\t\tHOTELS IN ERNAKULAM\n\t\t\t\t1.Holiday Inn\n\t\t\t\t2.Marriot\n\t\t\t\t3.Crown Plaza")
		er=input("Enter the Choice: ")
		if(er==1):
			print "It is ",ernakulam["Holiday Inn"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=ernakulam["Holiday Inn"]
				u="Holiday Inn"
		elif(er==2):
			print "It is ",ernakulam["Marriot"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=ernakulam["Marriot"]
				u="Marriot"
		elif(er==3):
			print "It is ",ernakulam["Crown Plaza"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=ernakulam["Crown Plaza"]
				u="Crown Plaza"
		else:
                        print("Invalid Choice")
	elif(ch==2):
		print("\n\t\t\t\tHOTELS IN Kozhikode\n\t\t\t\t1.Raviz\n\t\t\t\t2.The taj\n\t\t\t\t3.Kadavu")
		clt=input("Enter the Choice: ")
		if(clt==1):
			print "It is ",kozhikode["Raviz"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=kozhikode["Raviz"]
				u="Raviz"
		elif(clt==2):
			print "It is ",kozhikode["The Taj"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=kozhikode["The Taj"]
				u="The Taj"
		
		elif(clt==3):
			print "It is ",kozhikode["Kadavu"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=kozhikode["Kadavu"]
				u="Kadavu"
		else:
                        print("Invalid Choice")
	elif(ch==3):
		print("\n\t\t\t\tHOTELS IN Thrissur\n\t\t\t\t1.Joys Palace\n\t\t\t\t2.Lulu Convention Centre\n\t\t\t\t3.Dass Continental")
		tr=input("Enter the Choice: ")
		if(tr==1):
			print "It is ",thrissur["Joys Palace"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=thrissur["Joys Palace"]
		elif(tr==2):
			print "It is ",thrissur["Lulu Convention Centre"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=thrissur["Lulu Convention Centre"]
		elif(tr==3):
			print "It is ",thrissur["Dass Continental"]," per day"
			ch1=raw_input("Do you wish to Confirm Booking(y/n)\n\n")
			if(ch1=="y" or ch1=="Y"):
				pr+=thrissur["Dass Continental"]
		else:
                        print("Invalid Choice")
	else:
		print("Invalid Choice")
	t=0
if(ch>0 and ch<4 and t==0 and pr>0 ):
        rooms=input("Enter Number of Days of Stay :")
	print("\n1.Single Room\n2.Double Room(Extra 500 per Room)")
	k=input("\tEnter Choice: ")
	if(k==1):
		type="Single"
		pr+=0
	elif(k==2):
		pr+=500
		type="Double"
        pr*=rooms
        che=raw_input("Do you have a Promocode?(y/n)")
        if(che=="y" or che=="Y"):
                code=raw_input("ENTER PROMO CODE: ")
                if(code=="THOMAS"):
                        pr-=2500
			print " Congrats you just got a Discount of Rs 2500"
                elif(code=="CIRIL"):
                        pr-=3500
			print " Congrats you just got a Discount of Rs 3500"
                elif(code=="THAHSU"):
                        pr-=3000
			print " Congrats you just got a Discount of Rs 3000"
                else:
                        print "INVALID Promocode"
        print "\n\nYour Total Bill is for Rs ",pr
        n=raw_input("Confirm to Pay?(y/n)")
        if(n=="y" or n=="Y"):
                print "\n\tBooking Successfull \n\n<<<<<BILL>>>>>\nHotel: ",u,"\nType Of Room: ",type,"\nTotal Price :",pr
        else:
                print "\n\tBooking Unsuccessfull"
print("Thank You For using TCT\n\n\n\n\n\n\n\n\n\n\tCreators\n\t1.Ciril\n\t2.Thomas\n\t3.Thahsin")
	

		

