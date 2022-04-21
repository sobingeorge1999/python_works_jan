# bank
# ac creation  name,acc number,mininum
# with draw  amount
# deposit  amout

class Bank:
    bankname="sbi"
    def ac(self,name,acno):
        self.n=name
        self.acc=acno
        self.min=5000
        self.balance=self.min
    def deposit(self,amout):
        self.amout=amout
        self.balance=self.balance+self.amout
        print("your",Bank.bankname,"acc has crediated",self.amout)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("imsifficient")
        else:
            self.balance=self.balance-self.amnt
            print("acc debited with amount",self.amnt)
            print("balance ",self.balance)

ob=Bank()
ob.ac('hari',333)
ob.deposit(1200)
ob.withdraw(400)
ob.withdraw(233333)
