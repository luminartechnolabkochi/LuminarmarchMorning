#decorators

#
#
# def dec_div(func): #div(2,10)
#
#     def wrapper(no1,no2):#(2,10)
#         if no1<no2:#2<10
#             (no1,no2)=(no2,no1) #10,2
#         return func(no1,no2)
#     return wrapper
#
#
#
# @dec_div
# def div(no1,no2):
#
#     return no1/no2
#
# @dec_div
# def sub(no1,no2):
#     return no1-no2


def admin_required(fun):
    def wrapper(user,pin):
        if user != "admin":
            raise Exception("you are not able to perfoem")
        else:
            return fun(user,pin)
    return wrapper







@admin_required
def change_pin(user,pin):

    mypin=pin
    return mypin

@admin_required
def delete(user,username):
    return username + "deleted"

 print(change_pin("user1",201348))
try:
    print(change_pin("admin",201348))
except Exception as e:
    print(e.args)
try:
    print(delete("user1","ajay"))
except Exception as e:
    print(e.args)









# res=div(2,10)
# su=sub(2,10)
# print(su)




