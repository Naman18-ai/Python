'''write a program that asks the user to input a number a listed to be appended to an existing list.'''
previous_list=[1,2,3,4,5]
usr=eval(input("Enter the list or integers vo want to add to the list"))
if type(usr)==type([]):
    previous_list.extend(usr)
elif type(usr)==type(1):
    previous_list.append(usr)
else:
    print("Input a valid data type(List or integers)")
print("The generated list is",previous_list)    
        
    