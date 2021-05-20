#*args ,**args
#
# def add(num1,num2): #parameters num1,num2
#     return num1+num2

# add(10,20)

# add(10,20,30,40,50,60) #10,20,30

#aruments
#parameter


# def add(*arg):
#     result=0
#     for num in arg:
#         result+=num
#     return result
#
# print(add(10,20,30,40,50,50,50))



def print_employee(**args): #type fo args dictionary args={"id":1000,"name":"vishnu",}
    print(args)



print_employee(id=1000,name="vishnu",desig="developer",n_place="kozhikode",j_loc="kakkanad")



