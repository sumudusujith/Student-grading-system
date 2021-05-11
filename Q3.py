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