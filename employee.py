"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, contractRate = "", contractNumber = ""):
        self.name = name
        self.contractRate = contractRate
        self.contractNumber = contractNumber

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    
class MonthlyEmployee(Employee):

    def __init__(self, name, monthlyPay, contractRate = "", contractNumber = ""):
        super().__init__(name, contractRate, contractNumber)
        self.monthlyPay = monthlyPay
    
    def get_pay(self):
        pay = self.monthlyPay
        if self.contractNumber:
            pay += (self.contractNumber * self.contractRate)
        elif self.contractRate:
            pay += self.contractRate
        return pay
    
    def __str__(self):
        sentence = f"{self.name} works on a monthly salary of {self.monthlyPay}"
        if self.contractNumber:
            sentence += f" and receives a commission for {self.contractNumber} contract(s) at {self.contractRate}/contract"
        elif self.contractRate:
            sentence += f" and receives a bonus commission of {self.contractRate}"
        sentence += f". Their total pay is {self.get_pay()}."
        return sentence

class ContractEmployee(Employee):

    def __init__(self, name, hourlyPay, hours, contractRate = "", contractNumber = ""):
        super().__init__(name, contractRate, contractNumber)
        self.hourlyPay = hourlyPay
        self.hours = hours
    
    def get_pay(self):
        pay = (self.hourlyPay * self.hours)
        if self.contractNumber:
            pay += (self.contractNumber * self.contractRate)
        elif self.contractRate:
            pay += self.contractRate
        return pay

    def __str__(self):
        sentence = f"{self.name} works on a contract of {self.hours} hours at {self.hourlyPay}/hour"
        if self.contractNumber:
            sentence += f" and receives a commission for {self.contractNumber} contract(s) at {self.contractRate}/contract"
        elif self.contractRate:
            sentence += f" and receives a bonus commission of {self.contractRate}"
        sentence += f". Their total pay is {self.get_pay()}."
        return sentence


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, 600)


