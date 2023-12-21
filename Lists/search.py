'''search for an element in the given list of number'''
list=eval(input("Enter  a list!"))
length=len(list)
num=int(input("Enter the number to be searched"))
for i in range(length):
    if list[i]==num:
        print(num,"is found at the indexing",i)
        break
else:
    print("the element is not present in the list")    