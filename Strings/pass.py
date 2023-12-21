'''write a program that asks a username and code.Ensure that the user 
doesn't use their username as past of their code'''
username=input("Enter a username")
password=input("Enter a password")
if username in password:
    print("you password should not be in the username")
else:
    print("Your password is set")    