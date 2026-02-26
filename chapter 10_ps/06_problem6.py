from random import randint

class train:

    def __init__(slf, trainNo):
       slf.trainNo = trainNo

    def book(lila, fro, to):
        print(f"ticket is booked in train no: {lila.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train no: {self.trainNo} is running on timee")

    def getfare(self, fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(5, 50)}")

t = train(1)
t.book("mnr", "ktm")
t.getstatus()
t.getfare("mnr", "ktm")