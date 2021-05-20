# # #map() filter() print() input type
# # lst=[2,3,4,5,6,7]
# #
# #
# # # squares map()
# #
# #
# #
# #
# # squares=list(map(lambda num: num**2,lst))
# # print(squares)
# #
# #
# # names=["ajay","aravind","arun"]
#
#
#
#
#
#
# import functools
#
# lst=[7,8,9,4,3,2]
#
#
# #find sum of this list
# # map,filter lambada ? args
# # lambda 2 args
# #
# # total=functools.reduce(lambda no1,no2:no1+no2,lst)
# # print(total)
#
# highrst=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(highrst)
#
# #listcomprehension





# lst=[1,2,3,4,5]
#
# # squares
# squres=[ num**2 for num in lst]
# print(squres)
#
# fruits=["apple","orange","mango"]
#
# # [(apple,apple),(orange,orange),(mango,mango)]
#
#
#
# pairs=[ (fruit,fruit) for fruit in fruits ]
# print(pairs)
#
#



lst1=[10,20]
lst2=[30,40]


# [(10,30),(10,40),(20,30),(20,40)]
pairs_lst=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(pairs_lst)


#
# lst1=[1,2,3,4,5,6,7]
# #print evens
# #false,True,False
# evens=[num for num in lst1 if num%2==0]



# print(evens)




lst=[7,8,9,4,3,2]
lst.append(list(map(lambda num:num*num,lst)))
print(lst)

#num>5 num+1 num<5 num-1
# 8,9,10,3,2,1
# op=[num+1 if num>5 else num-1 for num in lst]
# print(op)

