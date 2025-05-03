from random_number_gen import random_number_gen as rng

print("Welcome to Bishow bank!")

user_name = [
    {"name": "Bishow Rai", "account_id": 123456, "account_pass": 2468},
    {"name": "Sita", "account_id": 12456, "account_pass": 24680},
    {"name": "Ram", "account_id": 1234567, "account_pass": 246800}
]

account_holder = input("Please Enter your name!: ")

found = False  # flag to track if user is found

def check_name(account_holder):
    for user in user_name:
        if user["name"].lower() == account_holder.lower():
           
            found = True
            return user

    if not found:
        print("Invalid name")



user= check_name(account_holder)


account_id = input("Please Enter your account id!")
account_pass = input("Please Enter your account password!")



def check_cred(id,passw):
    if int(id)==user["account_id"] and int(passw) == user["account_pass"]:
        user['token'] = rng()
        return user
    else:
        return "Invalid id or password.Please try again"

found_user=check_cred(account_id,account_pass)
print(found_user)

if check_cred(account_id,account_pass) == True:
    response  = input("1. To withdraw " \
    "2.check balance"\
    "3.Deposit")
    print(response)


