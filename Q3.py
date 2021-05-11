import time
#def for check the validity of the all credit marks inputs
def checkValidity(number): 
         if number % 20 == 0 and number <= 120 and number >= 0:
            check = True
            
         else:
            print("!^^^^range error^^^^!\n See intructions above(^_^)")
            check = False

            return check#to repeat range error 

print("                       !INSTRUCTIONS!")#intructions for users
print("")
print("")
time.sleep(2)
print("1:Enter your suitable credits when the programme ask it..")
time.sleep(2)
print("2:you can enter only you  ingers..")
time.sleep(2)
print("3:your credit must be below or equals 120..")
time.sleep(2)
print("4:your credit must be above or equals 0..")
time.sleep(2)
print("5:And finnaly your credit must be one of thease 0,20,40,60,80,100,120")
time.sleep(2)
print("")
print("")
print("")
print("^^^^^^^^^^^^^^^^^STUDENT_PROGRESSION_OUTCOME^^^^^^^^^^^^^^^^^")
print("")
print("Let's start to type your credits!!")
print("")
#count starts for inputs
progressCounter=0 
trailerCounter=0
donotCounter=0
excludeCounter=0
while True:
    sum_correct=False
    while sum_correct==False:#while
        

            credit_validation= False
            while credit_validation== False:
                try:
                    pass_credits=int(input("what is your pass credits :"))#pass credit input
                    credit_validation=checkValidity(pass_credits)
                    print("<---------------------------------------------->")
                    
                        
                except ValueError: #except for catch the value error
                    print("!^^^^integers required^^^^!\n See intructions above(^_^)")
                    credit_validation=False
            credit_validation= False
            while credit_validation== False: