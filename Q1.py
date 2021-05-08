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
print("2:you can enter only you  ingers..")
print("3:your credit must be below or equals 120..")
print("4:your credit must be above or equals 0..")
print("5:And finnaly your credit must be one of thease 0,20,40,60,80,100,120")
print("")
print("")
print("")
print("^^^^^^^^^^^^^^^^^STUDENT_PROGRESSION_OUTCOME^^^^^^^^^^^^^^^^^")
print("")
print("Let's start to type your credits!!")
print("")
sum_correct=False
credit_validation= False
        while credit_validation== False:
            try: 
               defer_credits=int(input("what is your defer credits :"))#defer credit input
               credit_validation=checkValidity(defer_credits)