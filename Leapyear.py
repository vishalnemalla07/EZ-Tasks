#Task - Leap Year
#write a code to check if a given year is a leap year or not using else if ladder
#Instructions:
#- Every year that is evenly divisible by 4, except for years that are evenly divisible by 100.
#- The years that are evenly divisible by 100 are leap years only if they are also evenly divisible by 400.
#- Ensure that your function handles these conditions accurately and efficiently.
 

n = int(input("Enter a year: "))
if(n % 4 == 0 and n % 100 != 0):
    print(f"{n} is a leap year!")
elif(n % 100 == 0 and n % 400 == 0):
    print(f"{n} is a leap year!")
else:
    print(f"{n} is not a leap year!")


