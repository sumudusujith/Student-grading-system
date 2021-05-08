#Q1
def checkValidity(number): #def for check the validity of the all credit marks inputs
         if number % 20 == 0 and number <= 120 and number >= 0:
            flag = True
	else:
            print("!!!!range error!!!!\n See intructions above(^_^)")
            flag = False

            return flag#to repeat to input again when range error occurred


print("                       !INSTRUCTIONS!")
print("")
print("")
print("1:Enter your suitable credits when the programme ask it..")