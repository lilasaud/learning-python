class employee:
    a = 1
class programmar(employee):
    b = 2
class manager(programmar):
    c = 3
o = employee()
print(o.a) #prints the a attribute
#print(o.b) # shows error as there is no b attribute in employee class

o = programmar()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)