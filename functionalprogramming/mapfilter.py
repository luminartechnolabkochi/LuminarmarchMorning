# arr=[2,3,4,5,6]
#
#
#
#
# # map(function?,iterable)
#
#
# squarelist=list(map(lambda num:num**2,arr))
# print(squarelist)
#
#
# lst=["ajay","arun","nikil","nivin"]
#
#
#
#
# uppername=list(map(lambda name:name.upper(),lst))
# print(uppername)
#
#
#





lst=[7,8,9,4,3,1]

# op=list(map(lambda num:num+1 if num>5 else num-1,lst))
# print(op)

# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)
#
#
# lst=["ajay","arun","nikil","nivin"]
#
# anmames=list(filter(lambda name:name[0]=='a',lst))
# print(anmames)

# print(),input(),type(),upper(),sort()
# function calling

#reduce

# functools
# import functools
from functools import *
arr=[1,2,3,4,5,6]


total=reduce(lambda num1,num2:num1+num2,arr)
print(total)


highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
print(highest)


#*args
#**kwargs
#ducktyping
#functionalprogramming
#   lambdafunction
#   map()
#   filter()
#   reduce()
#   list comprehension
#decorators?
#mysql
#Password@123
#mysql
#frontend
