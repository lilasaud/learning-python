class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("lila", 50000, 55667)
print(p.name, p.salary, p.pin, p.company)

b = programmer("bishal", 10000, 45678)
print(b.name, b.company, b.pin, b.salary )