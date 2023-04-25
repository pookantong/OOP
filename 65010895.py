import datetime

class Bank:
    def __init__(self, name, bank_id):
        self.__user_account = []
        self.__name = name
        self.__bank_id = bank_id
        
    def add_user(self, user):
        self.__user_account.append(user)
        
    def check_password(self, card_num, pin_password):
        user = self.find_user_by_card_num(card_num)
        if user.pin_password == pin_password:
            return {'status':True, 'user':user}
        else:
            return {'status':False}
    
    def find_user_by_card_num(self, card_num):
        for user in self.__user_account:
            if user.num == card_num: 
                return user
        
        

class ATM:
    def __init__(self, atm_id, amount_of_money):
        self.__atm_id = atm_id
        self.__amount_of_money = amount_of_money
        self.__bank = None
        
    def init_bank(self, bank):
        self.__bank = bank
        
    def start(self, card):
        while True:
            self.__insert_card = input('Please insert your card (Y/N): ')
            if self.__insert_card == 'y' or self.__insert_card == 'Y':
                self.__pin_password = input('Enter your PIN: ')
                self.__response = self.send_info_to_bank(card.num, self.__pin_password)
                self.__status = self.__response['status']
                if self.__status == True:
                    self.__current_user = self.__response['user']
                    self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
                else:
                    print('Account Incorrect')
                    
    
    def send_info_to_bank(self, card_num, pin_password):
        return self.__bank.check_password(card_num, pin_password)
    
    def select_transaction(self, type):
        if type == '1':
            self.withdraw()
        elif type == '2':
            self.deposite()
        elif type == '3':
            self.transfer()
            
    def amount_of_money_in_atm(self):
        return self.__amount_of_money['1000']*1000+self.__amount_of_money['500']*500+self.__amount_of_money['100']*100
    
    def withdraw(self):
        print('Available balance: ', self.__current_user.amount_of_money)
        self.__withdraw_amount = int(input('Enter amount to withdraw: '))
        self.__withdraw_cash = {'100':0, '500':0, '1000':0}
        if self.__withdraw_amount <= self.amount_of_money_in_atm() and self.__current_user.amount_of_money > self.__withdraw_amount:
            while self.__withdraw_amount > 0:
                if self.__withdraw_amount - 1000 >= 0:
                    self.__withdraw_cash['1000'] += 1
                    self.__withdraw_amount -= 1000
                elif self.__withdraw_amount - 500 >= 0:
                    self.__withdraw_cash['500'] += 1
                    self.__withdraw_amount -= 500
                elif self.__withdraw_amount - 100 >= 0:
                    self.__withdraw_cash['100'] += 1
                    self.__withdraw_amount -= 100
            if self.__withdraw_cash['1000'] > self.__amount_of_money['1000'] or self.__withdraw_cash['500'] > self.__amount_of_money['500'] or self.__withdraw_cash['100'] > self.__amount_of_money['100']:
                print('Not enough cash!!!')
                print('Balance: ', self.__current_user.amount_of_money)
                self.__withdraw_amount = None
                self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
            else:
                print('Number of 1000 bills: ',self.__withdraw_cash['1000'])
                print('Number of 500 bills: ',self.__withdraw_cash['500'])        
                print('Number of 100 bills: ',self.__withdraw_cash['100'])
                self.__amount_of_money['1000'] -= self.__withdraw_cash['1000']
                self.__amount_of_money['500'] -= self.__withdraw_cash['500']
                self.__amount_of_money['100'] -= self.__withdraw_cash['100']
                self.__current_user.amount_of_money -= (self.__withdraw_cash['1000']*1000+self.__withdraw_cash['500']*500+self.__withdraw_cash['100']*100)
                print('Balance: ', self.__current_user.amount_of_money)
                print('Number of 1000 bills in atm: ',self.__amount_of_money['1000'])
                print('Number of 500 bills in atm: ',self.__amount_of_money['500'])        
                print('Number of 100 bills in atm: ',self.__amount_of_money['100'])
                self.add_transaction('Withdraw', self.__withdraw_cash['1000']*1000+self.__withdraw_cash['500']*500+self.__withdraw_cash['100']*100)
                print(self.__current_user.transaction)
                self.__withdraw_cash = {'100':0, '500':0, '1000':0}
                self.__withdraw_amount = None
                self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
        elif self.__current_user.amount_of_money < self.__withdraw_amount:
            print('Not enough money in your account!!!')
            print('Balance: ', self.__current_user.amount_of_money)
            self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
        else:
            print('Not enough cash!!!')
            print('Balance: ', self.__current_user.amount_of_money)
            self.__withdraw_amount = None
            self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
    
    
    def transfer(self):
        print('Available balance: ', self.__current_user.amount_of_money)
        self.__transfer_account_num = int(input('Enter transfer account number: '))
        self.__transfer_user = self.__bank.find_user_by_card_num(self.__transfer_account_num)
        if self.__transfer_user == None or self.__transfer_user == self.__current_user:
            print('Invalid Transfer Account !!!')
            print('Balance: ', self.__current_user.amount_of_money)
            self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
        else:
            self.__transfer_amount = int(input('Enter amount to transfer: '))
            if self.__transfer_amount < self.__current_user.amount_of_money:
                self.__transfer_user.amount_of_money +=  self.__transfer_amount
                self.__current_user.amount_of_money -=  self.__transfer_amount
                print('Balance: ', self.__current_user.amount_of_money)
                self.add_transaction('Transfer',  self.__transfer_amount)
                self.__transfer_amount = None
                self.__transfer_user = None
                print(self.__current_user.transaction)
                self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
            else:
                print('Not enough money in your account!!!')
                print('Balance: ', self.__current_user.amount_of_money)
                self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
        
    def deposite(self):
        print('Available balance: ', self.__current_user.amount_of_money)
        self.__deposite_amount = int(input('Enter amount to deposite: '))
        self.__amount_of_money['1000'] += int(input('Number of 1000 bills: '))
        self.__amount_of_money['500'] += int(input('Number of 500 bills: '))
        self.__amount_of_money['100'] += int(input('Number of 100 bills: '))
        self.__current_user.amount_of_money += self.__deposite_amount
        print('Your deposite has been received\nBalance: ', self.__current_user.amount_of_money)
        print('Number of 1000 bills in atm: ',self.__amount_of_money['1000'])
        print('Number of 500 bills in atm: ',self.__amount_of_money['500'])        
        print('Number of 100 bills in atm: ',self.__amount_of_money['100'])
        self.add_transaction('Deposite',  self.__deposite_amount)
        print(self.__current_user.transaction)
        self.__deposite_amount = None
        self.select_transaction(input('Select transaction:\n1. Withdraw Cash\n2. Deposite Cash\n3. Transfer Money\ntransaction (1, 2, 3): '))
        
    def add_transaction(self, type, amount):
        self.__current_user.transaction.append(type+': '+str(amount))  
            
class Card:
    def __init__(self, card_id, first_name, last_name, num, expired_date):
        self.__card_id = card_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__num = num
        self.__expired_date = expired_date
    
    @property   
    def num(self):
        return self.__num
        
class UserAccount:
    def __init__(self, first_name, last_name, num, pin_password, amount_of_money):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__num = num
        self.__pin_password = pin_password
        self.__amount_of_money = amount_of_money
        self.__transaction = []
        
    @property   
    def pin_password(self):
        return self.__pin_password
    
    @property    
    def num(self):
        return self.__num
    
    def get_amount_of_money(self):
        return self.__amount_of_money
    
    def set_amount_of_money(self, new_amount_of_money):
        self.__amount_of_money = new_amount_of_money
        
    def get_transaction(self):
        return self.__transaction
    
    def set_transaction(self, new_transaction):
        self.transaction = new_transaction
    
    amount_of_money = property(get_amount_of_money, set_amount_of_money)
    transaction = property(get_transaction, set_transaction)


bank = Bank('pokantong', 123456789) 
atm_1 = ATM(1, {'100':1, '500':1, '1000':1})
card = Card(1, 'Yotsapat', 'Punyaworapan', 65010895, '25/04/2566')
user_1 = UserAccount('Yotsapat', 'Punyaworapan', 65010895, '0895', 1000)
user_2 = UserAccount('Yotsa', 'Punya', 65010896, '0896', 1000)

atm_1.init_bank(bank)
bank.add_user(user_1)
bank.add_user(user_2)

atm_1.start(card)

        