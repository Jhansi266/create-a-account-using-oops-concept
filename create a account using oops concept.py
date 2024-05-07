class account:
    def __init__(self,balance,accc):
        self.balance=balance
        self.accc=accc
    #debit
    def debit(self,amount):
        self.balance=self.balance-amount
        print("your account balance is",self.balance)
    #credit
    def credit(self,new):
        self.balance = self.balance +new
        print("your account balance is", self.balance)
    #total
    def bal(self):
        print("total amount",self.balance)

acc1=account(10000,123456)
print(acc1.balance)
print(acc1.accc)
acc1.debit(3000)
acc1.credit(2000)
acc1.bal()
