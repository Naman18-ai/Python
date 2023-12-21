'''program that reads a line and tell the number of different characters'''
string=input("Enter a string ")
lower=0
upper=0
alpha=0
digits=0
symbol=0
for i in i:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    elif i.isalpha():
        alpha+=1
    elif i.isdigit():
        digits+=1
    else:
        symbol+=1    
print(lower,'\n',upper,'\n',alpha,'\n',digits,'\n',symbol,'\n')         