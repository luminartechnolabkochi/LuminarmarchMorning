#lambada
#map
#filter
#reduce
#list

# ar=[2,3,4,5,6]
# squsres=[ num**2 for num in ar]
# print(squsres)
#
# firuits=["mango","apple","orange"]
#
# # [('mango','mango'),('apple','apple'),("orange","orange")]
#
# pairs=[ (fruit,fruit) for fruit in firuits]
# print(pairs)
#

lst1=[1,2]
lst2=[10,20]
# [(1,10),(1,20),(2,10),(2,20)]


pairs=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(pairs)



lst2=[10,11,12,13,14]


evens=[ num for num in lst2 if num%2==0]
print(evens)

lst2=[7,8,9,4,2]

# [8,9,10,3,1]

patttern=[num+1 if num>5 else num-1 for  num in lst2]
print(patttern)
