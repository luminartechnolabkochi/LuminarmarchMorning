#
# def add(num1,num2):
#     return num1+num2

# lambdafunction


# # def functionname retrun
# add = lambda num1, num2: num1 + num2
#
# print(add(10, 20))
#
# sub = lambda num1, num2: num1 - num2
#
# cube = lambda num: num ** 3
#
# print(cube(3))
#
# div = lambda num1, num2: num1 / num2
#
# print(div(10, 5))

# map()
# filter()
# reduce()

# [ajay,vijay,ram,ravi]    [1000,2000,3000,4000]

# 1 2 3 4 5
# f(sq(x))     upper()                         map()

# # (map)
# #1 4 9 16  25 AJAY VIJAY RAM RAVI
#
#
#
# lst=[1,2,3,4,5,6,7]      #[ajay,vijay,abi,ravi]  [1000,2000,3000,4000]
#
#   #condition f(num%2==0)    #
# #2 4 6                      #ajay abi                     2000,3000,4000
#
#
#
#
# #reduce
#
# lst=[1,2,3,4,5,6,7]    lst=[1,2,3,4,5,6,7]     st=[1,2,3,4,5,6,7]
#
# #28                            7                        1

from functools import reduce
employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 25000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]

# e_names=[ emp["name"].upper() for emp in employees]
# print("names====================",e_names)


# a_names=[emp["name"] for emp in employees if emp["name"][0]=='a']
# print("names====",a_names)


#salary above 23000


salry=[ emp for emp in employees if emp["salary"]> 23000 ]

print(salry)



# high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
#                 list(map(lambda emp:emp["salary"],employees)))
# print(high_sal)



# developers=list(filter(lambda emp:emp["designation"]=="developer" and  emp["salary"] >24000,employees))
# print(developers)

# sal_emp=list(filter(lambda emp:emp["salary"]>23000,employees))
# print(sal_emp)

# a_names=list(filter(lambda emp:emp["name"][0]=='a',employees))
#
# print(a_names)


# print employee names only map()
# e_names=list(map(lambda emp:emp["name"],employees))
# up_names=list(map(lambda name:name.upper(),e_names))
# print("names",up_names)







#print all employee name into uppercase  map()


#print employe deatails whose name starting with 'a'   ==a  filter()


#print employee details whode salary > 23000  filter()

#print employee details whose designation==developer

#print highest salary reduce


#print lowest salary reduce







for employee in employees:
    print(employee["name"])
