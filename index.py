from datetime import datetime
class Transaction:
   def __init__(self, date_time, narration, amount, transaction_type):
        self.date_time = date_time  
        self.narration = narration  
        self.amount = amount        
        self.transaction_type = transaction_type  
class Account():
    interest_rate= 0.05
    def __init__(self,account_holder, account_number):
        self._account_number = account_number
        self._account_holder = account_holder
        self._transactions = []
        self._loan_balance = 0.0
        self._is_frozen = False
        self._minimum_balance = 0.0
        self._is_closed = False
        
    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder

    def change_account_holder(self, name):
        if self._is_closed:
            return "Your account is closed."
        self._account_holder = name
        return f"Account owner changed to {name}"

    def _add_transaction(self, narration, amount, transaction_type):
        if self._is_closed:
            return "Your account is closed."
        transaction = Transaction(datetime.now(), narration, amount, transaction_type)
        self._transactions.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self._transactions:
            if transaction.transaction_type == 'credit':
                balance += transaction.amount
            elif transaction.transaction_type == 'debit':
                balance -= transaction.amount
        return balance

    def deposit(self, amount):
        if self._is_frozen:
            return "Account is frozen."
        elif amount <= 0:
            return "Deposit amount must be can not be negative"
        else:
          self._add_transaction("Deposit", amount, 'credit')
          return f"New balance: {self.get_balance():.2f}"
        
    
    def withdraw(self, amount):
        if self._is_frozen:
            return "Account is frozen."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        current_balance = self.get_balance()
        
        if amount > current_balance:
            return "Insufficient funds."
        else:
            self._add_transaction("Withdrawal", amount, 'debit')
        return f"New balance: {self.get_balance():.2f}"

    
    def transfer_funds(self, amount, recipient_account):
        if self._is_frozen:
            return "Your account is frozen."
        elif self._is_closed:
            return " accounts is closed"
        elif amount <= 0:
            return "Transfer amount must be positive."
        elif amount > self.get_balance():
            return "Insufficient funds."
        else:
            self._add_transaction(f"Transfer to {recipient_account}", amount, 'debit')
            
            return f"Your new balance: {self.get_balance():.2f}"


    def request_loan(self, amount):
        if self._is_closed:
            return "Account is closed."
        elif amount <= 0:
            return "Loan amount must be positive."
       
        else:
            self._loan_balance += amount
            self._add_transaction("Loan credited", amount, 'credit')
            return f"You have been given a loan of {amount:.2f}."

   
    def repay_loan(self, amount):
        if self._is_closed:
            return "Account is closed."
        elif amount <= 0:
            return "amount must be positive."
        current_balance = self.get_balance()
        if amount > current_balance:
            return "Insufficient funds"
        self._loan_balance -= amount
        self._add_transaction("Loan repayment", amount, 'debit')
        return f"Remaining loan balance: {self._loan_balance:.2f}"
     def view_account_details(self):
        details = (
            f"Account Number: {self._account_number}"
            f"Account Holder: {self._account_holder}"
            f"Current Balance: {self.get_balance():.2f}"
            f"Loan Balance: {self._loan_balance:.2f}"
           
        )
        return details

    
    def account_statement(self):
       
        for transactions in self._transactions:
            print(transactions)
        print(f"Current Balance: {self.get_balance()}")
    def apply_interest(self):
        if self._is_closed or self._is_frozen:
            return "Your account is closed or frozen."
        balance = self.get_balance()
        interest = balance * self.interest_rate
        self._add_transaction("Interest", interest, 'credit')
        return f"Interest of New balance: {self.get_balance():.2f}"
    def freeze_account(self):
        self._is_frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self._is_frozen = False
        return "Account has been unfrozen."

   
    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance is positive"
        self._minimum_balance = amount
        return f"Minimum balance is {amount:.2f}"

   
    def close_account(self):
        self._transactions.clear()
        self._loan_balance = 0.0
        self._is_closed = True
        return "Account closed."

