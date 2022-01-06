#Write a Function to check if year number is a leap year.
"""A leap year is exactly divisible by 4 except for century years (years ending with 00). 
The century year is a leap year only if it is perfectly divisible by 400."""

def leap(x):
   if (x%4==0) and (x%100==0):
      print("This is leap year")
   elif (x%100==0) and (x%400==0):
      print("This is leap year")
   else:
      print("Not leap year")
x=int(input("Enter a year"))
leap(x)





      
