
def admin_required(func):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("you are not allowed")
        else:
            return func(user,pin)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin

@admin_required
def delete_account(user,acno):
    return str(acno)+"deleted"




