class employee:
    language = "english" #This is a class attribute
    salary = 50000

    def __init__(self): # dunder method which is automatically called
        print("i am creating an object")
   
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")

lila = employee()
lila.name = "lila"
print( lila.name, lila.salary)

rohan = employee

