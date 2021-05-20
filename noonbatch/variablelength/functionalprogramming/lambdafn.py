#functional programming


#           3: return 3**3
cube=lambda num: num**3

print(cube(3))



# div

div=lambda num1,num2:num1/num2
print(div(2,4))


# hello h
#good  g
firstchar=lambda word:word[0]
print(firstchar("hai"))



# map()


# filter()


#reduce()



lst=[2,3,4,5,6]
# sq=[]
# for num in lst:
#     res=num**2
#     sq.append(res)

#2 3 4 5 6             2   filt(chkeven)====>2
                        # 3              =>
                        #4                  4
                        #5
                        #6                  6



#sq(f(x))


#4 9 16 25 36
# op squares of all objects



lst1=["ajay","aravind","ram","ravi"]

# ajay aravind



#upp(f(x))

#AJAY ARAVIND

# map()







employees=[
   {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]


#developers
developers=[ emp  for emp in employees if emp["designation"]=="developer"]
print(developers)

#highsal
sal=max([emp["salary"] for emp in employees])
print(sal)





#print employee names only
# enames=[emp["name"] for emp in employees]
# print(enames)


# developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
# developers_name=list(map(lambda emp:emp["name"],developers))
# print(developers_name)

# print developers name only




# filter developers


# names



# print all employees whose designation ==developer
#
# def get_developers(emp):
#
#     return emp["designation"]=="developer"
#            emp=   {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#
# developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
# print(developers)




# print employee names

#
# emp_names=list(map(lambda emp:emp["name"],employees))# {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"}
# print(emp_names)

# # print employee salaries
# e_sal=list(map(lambda emp:emp["salary"],employees))
# print(e_sal)



# lambda functions
#map()
#filter()