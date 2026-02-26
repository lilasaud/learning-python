class employee:
    
    language = "english" #This is a class attribute
    salary = 50000

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    @staticmethod
    def greet():
        print("good morning")

lila = employee()
#lila.language = "javascript" # This is an instance attribute
print( lila.language, lila.salary)

lila.getInfo()
lila.greet()
# Employee.getInfo(lila)

