class ATM:
    def __init__ (self,cardTaker,pinTaker):
        self.cardTaker = cardTaker
        self.pinTaker  = pinTaker
    def balanceEnquiry(self):
        print("your balance is $100")
    def CashWithdrawl(self,amount):
        cash = 100-amount
        difficultProject =input("You widthrawed : " + str(amount) + "Your remaining balance is : " + str(cash))


def main():
    cardTaker = input("Insert your card number :")
    pinTaker = input("Insert your pin :")
    user = ATM(cardTaker,pinTaker)
     
    print("SUCCESSFULL LOGIN")
    print("To check your Balance please press 1 and to widthraw cash pls press 2")
    activity = int(input("Enter activity of your choice :"))

    if(activity == 1):
     user.balanceEnquiry()
    elif(activity == 2):
        amount = int(input("Enter The Amount :"))
        user.CashWithdrawl(amount)
    else:
        print("inavlid number")

if __name__ == "__main__":
    main() 

