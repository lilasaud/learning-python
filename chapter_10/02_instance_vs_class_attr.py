class employee:
    
    language = "english" #This is a class attribute
    salary = 50000


lila = employee()
lila.language = "javascript" # This is an instance attribute
print( lila.language, lila.salary)

bishal = employee
print(bishal.salary)

# Here name is instance attribute and salary and  language are class attributes as they directly belong to the class