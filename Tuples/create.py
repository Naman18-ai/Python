'''create tuples from the following data type
1>"abcdef"
2>3,4,5,6
3>[11,12,13]
'''
string="abcdef"
integer=3,4,5
lists=[11,12,13]

t1=tuple(string)
t2=tuple(integer)
t3=tuple(lists)
print(t1,"\n",t2,"\n",t3,"\n")
