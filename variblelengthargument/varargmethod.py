


employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}



def print_employee(**kwargs): #kwargs={id:1003,prop:"salary"}
    id=kwargs["id"] #1000
    prop=kwargs["prop"] #  "salary"

    if id in employees: #1000 in employees

        print(employees[id][prop]) #"name":"ajay"

    else:
        print("invalid id")


print_employee(id=1003,prop="salary")# va

# create a function print_employee() =>calling fn print_employee(id=1000) it will name of that employee


# print_employee(id=1000) =>ajay
#print_employee(id=1000,prop="salary")ajay,25000

##print_employee(id=1001,prop="sdesignation")vijay,developer






