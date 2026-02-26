class Demo:
    a = 5

o = Demo() 
print(o.a) #prints the class attribute because instance attribute is not present


o.a = 0 # instance attribute is set
print(o.a) #prints the instancr attribute because instance attribute is  present


print(Demo.a) # prints the class attribute