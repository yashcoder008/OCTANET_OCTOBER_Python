class ATMUser:
    def __init__(self,userID,pin,balance):
        self.userId=userID
        self.pin=pin
        self.balance=balance
        self.transHistory=[]
    
    def getTransHistory(self):
        if len(self.transHistory)!=0:
             return self.transHistory
    
        else:
            print('NO TRANSACTION HISTORY')
        
    
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-=amount
            self.transHistory.append(f'WITHDRAWAL:₹{amount}')
            return True
        else:
            print("INSUFFICENT BALANCE.")
            return False
    def deposit(self,amount):
        self.balance+=amount
        self.transHistory.append(f'DEPOSIT:₹{amount}₹')
    def transfer(self,toUser,amount):
        if self.withdraw(amount):
            toUser.deposit(amount)
        
        self.transHistory.append(f'₹{amount} TRANSFER TO USER:{toUser.userId}')
        
def main():
    #ATM users:
    user1=ATMUser("810613","5118",5000)
    user2=ATMUser("630152","2799",2500)
    user3=ATMUser("970156","9405",6000)
    
    #ATM Operations:
    user=None
    while True:
        userId=input("ENTER USER ID:")
        userPin=input("ENTER PIN:")
        
        if userId==user1.userId and userPin==user1.pin:
            user=user1
        
        elif userId==user2.userId and userPin==user2.pin:
            user=user2
        elif userId==user3.userId and userPin==user3.pin:
            user=user3
        else:
            print("INVALID USER ID or PIN. PLEASE TRY AGAIN.")
            continue 
        while True:
            print("\n\n---SELECT AN OPTION---")
            print("1:TRANSACTIONS HISTORY")
            print("2:WITHDRAW")
            print("3:DEPOSIT")
            print("4:TRANSFER")
            print("5:QUIT")
            
            option= input("ENTER YOUR OPTION:")
            
            if option=="1":
                print("TRANSACTION HISTORY:")
                
                for transactions in user.getTransHistory():
                    print(transactions)
            elif option=="2":
                amount=float(input("ENTER AMOUNT TO WITHDRAW:₹"))
                user.withdraw(amount)
            elif option=="3":
                amount=float(input("ENTER AMOUNT TO DEPOSIT:₹"))
                user.deposit(amount)
            elif option=="4":
                
                while True: 
                    toUser=input("ENTER RECIVER'S USER ID:")
                    if toUser==user1.userId:
                        toUser=user1
                        break
                    elif toUser==user2.userId:
                        toUser=user2
                        break
                    elif toUser==user3.userId:
                        toUser=user3
                        break
                    else:
                        print("RECEVERS ID IS WRONG...TRY AGAIN!")
                        continue
                        
                amount=float(input("ENTER AMOUNT TO TRANSFER:₹"))
                user.transfer(toUser,amount)
            elif option=="5":
                print("THANK YOU FOR USING OUR ATM...GOODBYE! ")
            else:
                print("INVALID OPTION. PLEASE SELECT A VALID OPTION.")
main()
                
                
        
    