class DataEncapsulation:

    def __init__(self, balance):
        self.__balance_new = balance
        self.random=123
        #setting the .__balance as private so that cant be accessible outside the class


    def get_balance(self):
        return self.__balance_new

    def deposit_balance_in_account(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance_new += deposit_amount
            print(f"Deposit Amount: {deposit_amount}. New Balance: {self.__balance_new}")
        else:
            print("Invalid_amount")

obj = DataEncapsulation(1200)
# print(obj.get_balance())

obj.deposit_balance_in_account(700)






