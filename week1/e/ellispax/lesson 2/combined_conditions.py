#Using and & or conditions together.

#checking if two conditions are met using (and)

n1= int(input("Enter a number >> "))
n2 = int(input("Enter another number >> "))

#Conditional check using If & and
if n1 > 0 and n2 <100:
    print("Number between 1 and 100")
else:
    print("Number is out of range.")