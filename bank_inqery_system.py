print("Welcome to Bishow bank!")

account_id = input("Please Enter you account number!")
account_pass = input("Please Enter your account password")



def check_cred(id,passw):
    if int(id)==123456 and int(passw) == 2468:
        return True
    else:
        return "Invalid id or password.Please try again"

print(check_cred(account_id,account_pass))

if check_cred(account_id,account_pass) == True:
    response  = input("1. To withdraw " \
    "2.check balance"\
    "3.Deposit")
    print(response)


