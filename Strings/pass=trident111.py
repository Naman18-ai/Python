'''Write a  program that asks a user for a username and a passcode.
Make sure that passcode doesnot contain username and matches#trident111#'''


username=input("Enter a username ")
password=input("Enter a password")
if username not in password and password=="Trident111":
    print("your username and password is valid")
else:
    print("Choose a valid password")    
    