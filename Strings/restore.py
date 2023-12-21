'''write a program to input tro strings If string1 is contained in string2,then create a third string with 
first four characters os a string2, added with a word restore'''
s1=input("Enter a string")
s2=input("Enter another string")
if s1 in s2:
    print(s2[:5]+"\trestore")