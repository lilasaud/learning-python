import random
'''
1 for stone
-1 for paper
0 for scissor
'''

computer = random.choice([-1, 1, 0 ])
youstr = input("enter your choice: ")
youdict = {"st": 1, "p": -1, "s": 0}
reversedict = {1: "stone", -1: "paper", 0: "scissor"}
you = youdict[youstr]

print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("you win!")
    else:
        print("something wrong ")
        