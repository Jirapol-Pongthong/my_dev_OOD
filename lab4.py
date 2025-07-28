class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__accounts = []

    def get_citizen_id(self):
        return self.__citizen_id

    def get_name(self):
        return self.__name

    def get_accounts(self):
        return self.__accounts

    def add_account(self, account):
        self.__accounts.append(account)


    citizen_id = property(get_citizen_id)
    name = property(get_name)
    accounts = property(get_accounts)


class Account:
    def __init__(self, account_number: str, owner: User):
        self.__account_number = account_number
        self.__owner = owner
        self.__cards = []
        self.__balance = 0
        self.__transactions = []
    
    def get_account_number(self):
        return self.__account_number
    def get_owner(self):
        return self.__owner
    def get_cards(self):
        return self.__cards
    def get_balance(self):
        return self.__balance
    def get_transactions(self):
        return self.__transactions
    
    def set_transaction(self,transaction : str):
        self.__transactions.append(transaction)
        
    def set_cards(self,card):
        self.__cards.append(card)
        
    def set_balance(self, amount):
        self.__balance = amount    


    def show_transaction(self):
        transaction_lines = [f"{self.owner.name} transaction : {transaction}" for transaction in self.__transactions]
        return "\n".join(transaction_lines)

    
    def deposit(self,amount):
        if isinstance(amount,int):
            if amount > 0 :
                self.__balance += amount
                return self.__balance
            else:
                return 'can not deposit'
            
    def withdraw(self,amount):
        if isinstance(amount,int):
            if  self.__balance < amount:
                return 'Error'
            if amount < 0 :
                return 'can not withdraw'
            self.__balance -= amount
            return self.__balance

    def ac_transfer(self, next_account, amount):
        if amount < 0 :
            return 'can not transfer'
        withdraw = self.withdraw(amount)

        if isinstance(withdraw,str):
            return withdraw
        deposit = next_account.deposit(amount)  
        return deposit
    
    account_number = property(get_account_number)
    owner = property(get_owner)
    cards = property(get_cards)
    balance = property(get_balance,set_balance)
    tranaction = property(get_transactions)



class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin

    def get_card_number(self):
        return self.__card_number
    def get_account(self):
        return self.__account
    def get_pin(self):
        return self.__pin
    
    card_number = property(get_card_number)
    account = property(get_account)
    pin = property(get_pin)
    
class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__initial_amount = initial_amount
    
    def get_machine_id(self):
        return self.__machine_id
    def get_initial_amount(self):
        return self.__initial_amount
    def set_initial_amount(self,amount):
        self.__initial_amount = amount

    def insert_card(self,id_machine : str,atm_number :str ,pin :str, bank: 'Bank'):
        if self.__machine_id == id_machine :

            for user in bank.users:
                for account in user.accounts:
                    for card in account.cards:
                        if  card.card_number == atm_number:
                            if card.pin == pin :
                                return account
                            else :
                                return 'Invalid'
        else :
            return 'Invalid'
    
    def atm_deposite(self,id_machine : str,atm_number : str ,pin :str,amount :int,bank : 'Bank'):

        if self.__machine_id != id_machine:
            return "Invalid"

        if amount <= 0:
            return "Error"

        for user in bank.users:
            for account in user.accounts:
                for card in account.cards:
                    if card.card_number == atm_number:
                        if card.pin == pin:

                            before_balance = account.balance
                            last_balance = account.deposit(amount)

                            if isinstance(last_balance, str):  
                                return last_balance

                            
                            self.__initial_amount += amount
                            transaction = f"D-ATM:{self.__machine_id}-{before_balance}-{last_balance}"
                            account.set_transaction(transaction)

                            return f"{user.name} account before test: {before_balance}, account after test: {last_balance}"

                        return "Error: Invalid PIN."
        return "Error"


    
    def atm_withdraw(self,id_machine,atm_number,pin,amount,bank:'Bank'):
        if self.__machine_id != id_machine:
            return 'Invalid'
        if amount <= 0 :
            return 'can not withdraw'
        if amount > 40000:
            return 'money in atm have not enough'
        if amount > self.initial_amount:
            return 'money in atm have not enough'
        
        for user in bank.users:
            for account in user.accounts:
                for card in account.cards:
                    if card.card_number == atm_number:
                        if card.pin == pin:

                            before_balance = account.balance
                            last_balance = account.withdraw(amount)

                            if isinstance(last_balance, str):  
                                return last_balance

                            
                            self.__initial_amount -= amount
                            transaction = f"W-ATM:{self.__machine_id}-{before_balance}-{last_balance}"
                            account.set_transaction(transaction)

                            return f"{user.name} account before test: {before_balance}, account after test: {last_balance}"

                        return "Invalid"
            
                    
    def transfer(self, id_machine, atm_number, pin, second_number, amount, bank: 'Bank'):
        if self.__machine_id != id_machine:
            return "Invalid ATM machine"
        
        if amount <= 0:
            return "Invalid amount"

        first_account = None
        second_account = None
        first_user = None
        second_user = None

        for user in bank.users:
            for account in user.accounts:
                for card in account.cards:
                    if card.card_number == atm_number:
                        if card.pin == pin:
                            first_account = account
                            first_user = user.name
                        else:
                            return "Error"

        for user in bank.users:
            for account in user.accounts:
                if account.account_number == second_number:
                    second_account = account
                    second_user = user.name

        if not first_account:
            return "Error"
        if not second_account:
            return "Error"

        if first_account.balance < amount:
            return "Error"

        first_balance_before = first_account.balance
        second_balance_before = second_account.balance

        first_account.balance -= amount
        second_account.balance += amount

        first_balance_after = first_account.balance
        second_balance_after = second_account.balance


        first_account.set_transaction(f"TD-ATM:{self.__machine_id}-{first_balance_before}-{first_balance_after}")
        second_account.set_transaction(f"TD-ATM:{self.__machine_id}-{second_balance_before}-{second_balance_after}")

        return (f"{first_user} account before: {first_balance_before}, account after: {first_balance_after} "+ '\n'
                f"{second_user} account before: {second_balance_before}, account after: {second_balance_after}")

    
    def show_history_transactions(self, machine_id: str, atm_number: str, pin: str, bank: 'Bank'):
        if self.__machine_id != machine_id:
            return "Invalid"
        for user in bank.users:
            for account in user.accounts:
                for card in account.cards:
                    if card.card_number == atm_number:
                        if card.pin == pin:
                            return account.show_transaction()
                        else:
                            return "Invalid"
                        
    
    machine_id = property(get_machine_id)
    initial_amount = property(get_initial_amount,set_initial_amount)

class Bank:
    def __init__(self):
        self.__users = [] 
        self.__atm_machines = []  

    def get_user(self):
        return self.__users
    def get_atm_machines(self):
        return self.__atm_machines
    
    def set_user(self,user :User):
        self.__users.append(user)

    def set_atm_machines(self, atm : ATMMachine):
        self.__atm_machines.append(atm)

    users = property(get_user)
    atm_machines = property(get_atm_machines)


##################################################################################

# กำหนดให้ ชื่อคลาส (Class Name) ต้องเป็น Pascal case เช่น BankAccount
# กำหนดให้ ชื่อ instance และ variables ใดๆ ต้องเป็น snake case เช่น my_book
# กำหนดให้ เมื่อรับพารามิเตอร์เข้าใน method ต้องทำ validate data type และกรอบของค่า parameter ก่อนใช้เสมอ
# กำหนดให้ method ที่จัดการข้อมูลใด ต้องอยู่ในคลาสนั้น และพยายามอย่า access attribute นอกคลาส

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM , จำนวนเงิน]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

def create_instance():
    bank = Bank()
    
    for citizen_id, data in user.items():
        name, account_number, card_number, balance = data
        user_instance = User(citizen_id, name)
        account_instance = Account(account_number, user_instance)
        account_instance.balance = balance
        atm_card_instance = ATMCard(card_number, account_instance, pin="1234")
        
        user_instance.add_account(account_instance)
        account_instance.set_cards(atm_card_instance)
        
        bank.set_user(user_instance)
        
    for machine_id, initial_amount in atm.items():
        atm_instance = ATMMachine(machine_id, initial_amount)
        bank.set_atm_machines(atm_instance)
        
    return bank

bank = create_instance()

atm_machine = bank.atm_machines[0]
atm_machine2 = bank.atm_machines[1]

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

account = atm_machine.insert_card('1001', '12345', '1234', bank)
if isinstance(account, Account):
    for card in account.cards:
        cardnum = card.card_number
    print(f"{cardnum} , {account.account_number} , Success")
print("")

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000

test2 = atm_machine.atm_deposite('1001', '12346', '1234', 1000, bank)
print(test2)
print("")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
test3 = atm_machine2.atm_deposite('1002', '12346', '1234', -1, bank)
print(test3)
print("")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

test4 = atm_machine2.atm_withdraw('1002', '12346', '1234', 500, bank)
print(test4)
print("")

# # Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# # ผลที่คาดหวัง : แสดง Error

test5 = atm_machine2.atm_withdraw('1002', '12346', '1234', 2000, bank)
print(test5)

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

test6 = atm_machine2.transfer('1002', '12345', '1234', '0987654321',10000, bank)
print(test6)
print("")

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500
test7 = atm_machine2.show_history_transactions('1002', '12346', '1234', bank)
print(test7)
print("")


# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
# atm_machine = bank.atm_machines('1001')
# test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN

test8 = atm_machine.insert_card('1001', '12345', '9999', bank)
print(test8) 
print("")


# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
account = atm_machine.insert_card('1001', '12345', '1234', bank)
if isinstance(account, Account):
    harry_balance_before = account.balance
    print(f"Harry account before test: {harry_balance_before}")
    print("Attempting to withdraw 45,000 baht...")
    result = atm_machine.atm_withdraw('1001', '12345', '1234', 45000, bank)
    print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
    print(f"Actual result: {result}")
    print(f"Harry account after test: {account.balance}")
    print("-------------------------")
else:
    print(account)

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
if isinstance(account , Bank):
    account = atm_machine.insert_card('1001', '12345', '1234', bank)
    print("Test case #10 : Test withdrawal when ATM has insufficient funds")
    print(f"ATM machine balance before: {atm_machine.balance}")
    print("Attempting to withdraw 250,000 baht...")
    result = atm_machine.withdraw(account, 250000)
    print(f"Expected result: ATM has insufficient funds")
    print(f"Actual result: {result}")
    print(f"ATM machine balance after: {atm_machine.balance}")
    print("-------------------------")


# TODO 1 : จากข้อมูลใน user ให้สร้าง instance ของผู้ใช้ โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
# TODO :   ต้อง validate ข้อมุลทุกอย่าง ก่อนสร้าง instance ใดๆ




# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี



# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
# atm_machine = bank.atm_machines('1001')
# test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
# atm_machine = bank.get_atm('1001')
# account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
# harry_balance_before = account.get_balance()

# print(f"Harry account before test: {harry_balance_before}")
# print("Attempting to withdraw 45,000 baht...")
# result = atm_machine.withdraw(account, 45000)
# print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
# print(f"Actual result: {result}")
# print(f"Harry account after test: {account.get_balance()}")
# print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
# atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
# account = atm_machine.insert_card('12345', '1234')

# print("Test case #10 : Test withdrawal when ATM has insufficient funds")
# print(f"ATM machine balance before: {atm_machine.get_balance()}")
# print("Attempting to withdraw 250,000 baht...")
# result = atm_machine.withdraw(account, 250000)
# print(f"Expected result: ATM has insufficient funds")
# print(f"Actual result: {result}")
# print(f"ATM machine balance after: {atm_machine.get_balance()}")
# print("-------------------------")