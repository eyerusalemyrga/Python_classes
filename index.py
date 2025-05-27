class Account:
    def __init__(self,name):
        self.name=name
        self.deposits=[]
        self.balance=0
        self.withdraws=[]
        self.transfers=[]
        self.loan=0
        self.payment=[]
        self.mimimum_balance=100
        self.is_frozen=False
        self.is_closed=False
        self.transactions=[]
        
    def deposit(self,amount):
        if self.is_frozen==False and self.is_closed==False:
           self.balance+=amount
           self.deposits.append(amount)
           self.transactions.append(amount)
        return f"Hello {self.name}, you have received {amount}. Your new balance is {self.balance}"
# deposit, withdraw, show_balance, transfer, Loan, repay_loan, get_statement, get_loan statement
    
    
    def withdraw(self, withdraw_amount):
         if self.is_frozen==False and self.is_closed==False: 
            if withdraw_amount>=self.balance:
               return f"{withdraw_amount} can not be withdraw. Your balance is insufficient."
            else:
               self.balance-=withdraw_amount
               self.withdraws.append(withdraw_amount)
               self.transactions.append(withdraw_amount)
            return f"{withdraw_amount} amount of money has been withdrawn. your new balance is {self.balance}"

    def transfer(self, transfered_amount, received_name):
        if self.is_frozen==False and self.is_closed==False: 
       
          if transfered_amount< self.balance and self.balance>=0:
           self.balance-=transfered_amount
           self.transfers.append(transfered_amount)
           self.transactions.append(transfered_amount)

           return f"{transfered_amount} is being transferred to {received_name}. Your new balance is {self.balance}"
          elif transfered_amount> self.balance or self.balance<=0:
           return f"You can not transfer {transfered_amount} amount of money"
          else:
           return f"You can not transfer {transfered_amount}. Your balance is insufficient."
    def Get_balance(self):
        if self.is_frozen==False and self.is_closed==False: 
           sum_deposits=sum(self.deposits)
           sum_withdraws=sum(self.withdraws)
           balance=sum_deposits-sum_withdraws
           return balance
            
  
    def request_loan(self):
        if self.is_frozen==False and self.is_closed==False: 
           if self.balance>=12000:
            self.transactions.append()
            return f"{self.loan} was given to you."
           else:
            return f"loan is only given for those who have 12000birr in their account"
    def payment_loan(self,payed_amount):
        if self.is_frozen==False and self.is_closed==False: 
           self.payment.append(payed_amount)
           self.transactions.append(payed_amount)
           if self.loan>0:
             loan_amount=self.loan-payed_amount
             return f"You have paid {payed_amount}. The remaining loan is {loan_amount}"
           else:
             return f"You have no loan to pay"
    def View_account_details(self):
        return f"You have deposited: {self.deposits}, withdwrew: {self.withdraws}, transferred: {self.transfers}. you have {self.balance}Birr of money in your account."
    def change_owner(self):
        if self.is_frozen==False and self.is_closed==False: 
           self.name="Milen"
           return f"{self.name} is the owner of the account now."
    def account_statement(self):
        if self.is_frozen==False and self.is_closed==False: 
           for transactions in self.transactions:
            return f"{transactions}"
    def interest_calculation(self):
        if self.is_frozen==False and self.is_closed==False: 
           interest=0.05*self.balance
           new_balance=0.05*self.balance +self.balance
           return f"Hello {self.name} Your new balance is {new_balance}. interest balance is {interest}"
    def freeze_account(self):
        
        if self.is_frozen==True:
            return f"Your account is being freezed"
        else:
            return f"The account is active."
    def unfreeze_account(self):
        
          if self.is_frozen==True:
            return f"Your account is being freezed"
          else:
            return f"The account is active."
    def Set_minimum_balance(self, withdraw_amount):
        if self.is_frozen==False and self.is_closed==False: 
           if self.balance<=self.mimimum_balance:
            return f"withdraw can not be done with {self.balance}"
           else:
            return f"{withdraw_amount} amount of birr is being withdrew"
    def close_account(self):
        self.balance=0
        self.loan=0
        if self.is_closed==True:
            return True
        else:
            return False

        
accountone=Account("Eyeru")
print(accountone.deposit(100))
print(accountone.withdraw(120))
print(accountone.transfer(80, "letemeskel"))
print(accountone.request_loan())
print(accountone.payment_loan(100))
print(accountone.View_account_details())
print(accountone.change_owner())
print(accountone.account_statement())
print(accountone.interest_calculation())
print(accountone.freeze_account())
print(accountone.Set_minimum_balance(80))
print(accountone.close_account())
print(accountone.Get_balance())
print(accountone.unfreeze_account())