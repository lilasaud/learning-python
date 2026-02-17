'''
factorial(n) = n X n-1 x.......3 x 2 x 1

factorial(n) = n* factorial(n-1)

'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)
 


n = int(input("enter a number: ")) 
print(f"the factorial of this number is: {factorial(n)}")
