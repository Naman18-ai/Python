'''Create a copy of a list and add 10 to the first and the last element of the copied list'''
a=[1,23,34,45,62,52,25,66,77]
b=list(a)
b[0]+=10
b[-1]+=10
print(b)