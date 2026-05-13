''' CLASSS deep diving
    (1) ENCAPSULATION 
    (2) INHERITANCE 
    (3) POLIMORPHISM
'''

print("========  (1) ENCAPSULATION   ========")
# ENCAPSULATION  > public __private  _protected
'''
C++ JAVA > public private protected
PHP Typescript > public private protected
Python > public __private  _protected
'''


class Account():

    # state
    description = "The class make bank accounts"

    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("* deposit executed*")
        self.__amount += amount

    def withdraw(self, amount):
        print("* withdraw executed*")
        self.__amount -= amount

    @property   # bu orqali biz private malumotni ko'rishimiz mumkin ekan
    def holder(self):
        return self.__owner

    @holder.setter      # bu setter usul bilan owner malumotini o'zgartirsak bo'lar ekan. Bu orqali statelar bilan o'zgartirsak bo'lar ekan
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    # bu bizning doimiy ishlatib kelayotgan yo'limiz ekan
    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-----")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()


print("-----")
# my_account.amount = 1000000
# my_account.owner = "ADAM"
# my_account.amount = 10000000
# my_account.get_balance()
# print(my_account.owner)

try:
    result = my_account.amount
    print("result", result)
except Exception as err:
    print("No target state found:", err)


# geter vs setter

# account_owner = my_account.holder
# print("account_owner:", account_owner)
print("current owner before:", my_account.holder)  # state
# my_account.change_ownership("Adam")
my_account.holder = "Adam"  # state
print("current owner after:", my_account.holder)
