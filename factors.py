
'''this program determines which numbers in the list
        can be DIVIDED  INTO X without a remainder, aka  [ % == 0 ] '''
import time
def factors(x):  
    for n in range(1,x+1):              
        if x % n == 0 :
            print ('\n Factor: ', n)
            time.sleep(0.1)
    print("End")
    print()

num = int(input("Enter a number to see its factors: "))
factors(num)
