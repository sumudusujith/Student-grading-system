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
while sum_correct==False:

        credit_validation= False
        while credit_validation== False:
            try:
                pass_credits=int(input("what is your pass credits :"))#pass credit input
                credit_validation=checkValidity(pass_credits)
                print("----------------------------------------------")
                
                    
            except ValueError: #except for catch the value error
                print("!^^^^integers required^^^^!\n See intructions above(^_^)")
                credit_validation=False
        credit_validation= False
        while credit_validation== False:
            try: 
               defer_credits=int(input("what is your defer credits :"))#defer credit input
               credit_validation=checkValidity(defer_credits)
              
               print("-----------------------------------------------")
            
            except ValueError: #except for catch the valuer error
                print("!^^^^integers required^^^^!\n See intructions above(^_^)")
                credit_validation=False
                
        credit_validation= False
        while credit_validation== False:
             try:
                 fail_credits=int(input("what is your fail credits:"))#fail credit input
                 credit_validation=checkValidity(fail_credits)
                 
                 
                 print("----------------------------------------------")
             except ValueError: #except for catch the value error 
                  print("!^^^^integers required^^^^!\n See intructions above(^_^)")
                  credit_validation=False 


        total_credits=( pass_credits , defer_credits , fail_credits )#sum of the credits of a student
        total=sum(total_credits)

        if total==120: #condition for total credits
                           sum_correct=True
        else :        
                      print("*^^^^total incorrect^^^^*\n See intructions above(^_^)")
           
if(pass_credits==120) :
      print("~~*----progress----*~~")
       
elif(fail_credits>=80):
       print("~~*----excluded----*~~")
elif(pass_credits==100):
       print("~~*----Progress ??? module traileler----*~~")
else :
       print("~~*----Do not progress ??? module retriever----*~~")


print("                    THANK YOU!")
print("          !!!!!!!programme is over!!!!!!!")
exit()       
                                   
                           
                    
            

                    
           
