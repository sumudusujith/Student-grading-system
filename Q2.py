#Q2
#def for check the validity of the all credit marks inputs.
import time
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
#count starts for inputs
number_stud=0
progressCounter=0 
trailerCounter=0
donotCounter=0
excludeCounter=0