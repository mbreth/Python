# More practice of using classes in python (12/28/2019)

import time

class website():    
    def __init__(self, username):
        self.username = username

    def loginPass(self, password):
        _pass = ["Python!", "dragonBall", "Uniden1"]
        for words in _pass:
            if password == words:
                print("Login successful!")
                break
        if password not in _pass:
            print("Incorrect password. Redirecting you to security.")

    def loginID(self, user):
        global loginSuccess
        _name = ["mbreth", "samWilson", "Dpurcell"]
        for names in _name:
            if user == names:
                loginSuccess += 5
                print("Welcome {}!".format(user))
                break
        if user not in names:
            print("Records not available")
            loginSuccess = 0

    def createAcc(self, new_name, new_pass):
        print("Creating account...")
        time.sleep(3)
        print("Account creation successful!")
        print("Welcome to Brethbook, {}!".format(new_name))        

loginSuccess = 0
login = input("What is your username?: ")
user = website(login)
user.loginID(login)
if loginSuccess > 0:
    pass_ = input("What is your password?: ")
    user.loginPass(pass_)
elif loginSuccess == 0:
    print("No records are here for you.")
    print("You can create an account if you want to?: ")
    creAcc = input()
    if creAcc == "yes":
        new_name = input("What is your username going to be?: ")
        new_pass = input("What is your password going to be?: ")
        user.createAcc(new_name, new_pass)
    else:
        print("Have a great day. Goodbye!")
