

expences=[23000,15000,17000,18000]


month=int(input("enter mont to print element 1)jan 2)feb 3)march 4)april"))

try:
    print("expense",expences[month])

except Exception  as  e:
    print(e.args)

no1=int(input("enter no1"))
no2=int(input("enter no2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)