a = int(input("enter your age: "))
# if statement no:1
if(a%2==0):
    print("you have entered even number")
# end of if statement no:1
# if statement no:2
if (a>=18):
    print("you are eligible to vote")

elif(a<0):
    print("invalid age")

else:
    print("you are not eligible to vote")
# end of if statement no:2
print("end of program")