"""bulit in exception error:
1:ZerodivisionError 1/0
2:IndexError - when index is out of range
3:NameError - when variable not found
4:SyntaxError - raise by parser when a syntax error is encountered
5:Inbuilt overflow -> when value exceeed"""



import time

m=0
print(" ")
print("*******Give inputs*******")
print(" ")

while True:
    try:

        m=int(input("Enter minutes? "))
        while m<=0:
            raise Exception("Oops! That was not a valid number. Try again")
        break
    except ValueError:
        print("Please type number!")

def hour(m):
    if m>0:
        hour=m//60
        minute=m%60
        return hour,minute
i,j=hour(m)        
print("{} hour {} minutes".format(i,j))        

time.sleep(2)
