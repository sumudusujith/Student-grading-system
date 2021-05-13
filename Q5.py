
import time#import time for print time late
results=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]#main list
countA=0#count for progress
countB=0#count for Progress – module trailer
countC=0#count for Do not progress – module retriever
countD=0#count for excluded 
for appendix in range(len(results)):#loop for 10 outcomes
        
	print('!!!Student-Progress outcome!!!')
	time.sleep(3)
	print('pass_Credit : ',results[appendix][0])#indexing for pass_credit
	print('defer_Credit: ',results[appendix][1])#indexing for defer_credit
	print('fail_Credit : ',results[appendix][2])#indexing for fail_credit
	print("")
	print('Final output')
	print("\/\/\/\/\/\/\/")
	print("")

	pass_credit=results[appendix][0]
	defer_credit=results[appendix][1]
	fail_credit=results[appendix][2]




       
        
	if pass_credit==0 and defer_credit <= 40:
		print("Exclude")
		countD+=1
		
	elif pass_credit == 0 and 40<=defer_credit<=120:
		print("Do not Progress-Module Retriever")
		countC+=1
	
	elif pass_credit == 20 and 0<= defer_credit<=20:
		print("Exclude")
		countD+=1
	elif pass_credit==20 and 20< defer_credit <= 100:
		print("Do not Progresss -Module Retriever")
	elif pass_credit==40 and defer_credit==0:
		print("Exclude")
		countD+=1

	elif pass_credit==40 and 0< defer_credit <= 80:
		print("Do not Progress-Module Retriever")
		countC+=1