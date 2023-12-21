'''Gain an string as an input and ask the user for aan integer to find in the string is present'''
a=input("Enter the string here")
b=int(input("Enter the integer to be searched in the string"))
c=str(b)
if c in a:
    print("the number is present")
else:
    ("it is not here")    