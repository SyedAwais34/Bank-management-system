import json 
import random
import string
from pathlib import Path




class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")        
    except Exception as err:
        print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)





    def Createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age": int(input("Tell your age :- ")),
            "email": input("Tell your email :- "),
            "pin": int(input("Tell your 4 digit pin :-")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number. Thanksyou")    

            Bank.data.append(info)    

            Bank.__update()


    def depositmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your 4 digit pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to deposit :- "))   
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update() 
                print("Amount despoit successfully")




    def withdrawmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your 4 digit pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to withdraw :- "))   
            if userdata[0]['balance'] < amount:
                print("Sorry you can don't have that much money")

            else:
                userdata[0]['balance'] -= amount
                Bank.__update() 
                print("Amount withdrawn successfully")  



    def showdetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your 4 digit pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your Information are \n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your 4 digit pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such user found")

        else:
            print("You cannot change the age, accountNo. and your balance")

            print("Fill the details for change and leave it empty if no change")    

            newdata = {
                "name" : input("Please tell new name or press enter :- "),
                "email" : input("Please tell your new email and press enter to skip :- "),
                "pin" : input("Enter new pin or press enter to skip :- ")
            }

            if newdata["name"] == "" :
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "" :
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "" :
                newdata["pin"] = userdata[0]["pin"]

            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]    

            Bank.__update()                    
            print("Details updated successfully")


    def deleteaccount(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your 4 digit pin :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no such data exists")
        else:
            check = input("Press y if you actually want to delete your account or press n to bypass :- ")

            if check == 'n' or check == 'N':
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])    
                Bank.data.pop(index)
                print("Account deleted successfully")        
                Bank.__update()



user = Bank()
print("Press 1 for creating a account ")
print("Press 2 for deposit the money in the bank ")
print("Press 3 for withdraw the money ")
print("Press 4 for details ")
print("Press 5 for updating the details ")
print("Press 6 for deleting your account ")

check = int(input("Tell your response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney() 

if check == 4:
    user.showdetails() 

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()
