class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square iss {self.n*self.n}")



    def cube(self):
     print(f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
     print(f"the squareroot is {self.n**1/2}")
    
    @staticmethod
    def hellow():
       print("hellow there!!")

    

a = calculator(2)
a.hellow()
a.cube()
a.square()
a.squareroot()