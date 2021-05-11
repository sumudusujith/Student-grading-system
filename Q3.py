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
                try: 
                    defer_credits=int(input("what is your defer credits :"))#defer credit input
                    credit_validation=checkValidity(defer_credits)
              
                    print("<----------------------------------------------->")
             
                except ValueError: #except for catch the valuer error
                    print("!^^^^integers required^^^^!\n See intructions above(^_^)")
                    credit_validation=False
                
            credit_validation= False
            while credit_validation== False:
                try:
                    fail_credits=int(input("what is your fail credits:"))#fail credit input
                    credit_validation=checkValidity(fail_credits)
                 
                 
                    print("<---------------------------------------------->")
                except ValueError: #except for catch the value error 
                    print("!^^^^integers required^^^^!\n See intructions above(^_^)")
                    credit_validation=False 

            total_credits=( pass_credits, defer_credits , fail_credits )#total marks of the student
            total=sum(total_credits)

            if total==120: 
                               sum_correct=True
            else :
                          print("!^^^^total incorrect^^^^!\n See intructions above(^_^)")
               
            if(pass_credits==120):
                  print("progress")
                  progressCounter+=1#counting one per one input
             
            elif(fail_credits>=80):
                   print("excluded")
                   excludeCounter+=1#counting one per one input
            elif(pass_credits==100):
                   print("Progress – module trailer")
                   trailerCounter+=1#counting one per one input
            else :
                   print("Do not progress – module retriever ")
                   donotCounter+=1#counting one per one input
                                           
  #continue or print histogram
    while True:
        
            Exit=input("if you want to exit program press ----->'q' \npress ----->'p'<---- to continue with the next student\n" )
            if Exit.lower()=="p":#to continue
                break
            elif Exit.lower()=="q":
                break
               
            else :
                  print("invalid input please enter'q' or 'p'")
                
    if Exit.lower()=="q":
       break

Max=max( progressCounter,trailerCounter,donotCounter,excludeCounter)
#1st row of the histogram
print("progress trailing retriever  excluded")#head topics of table
time.sleep(3)
for count in range(0,Max):