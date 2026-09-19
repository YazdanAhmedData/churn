# greatest of 3 numbers using functions

# def greatest(a,b,c):
#     if(a>b and a>c):
#       print("a is greatest")
#     elif(b>a and b>c):
#       print("b is the greatest number")
#     else:
#        print("c is the greatest number") 


# a =int(input("enter a number"))
# b =int(input("enter a number"))
# c =int(input("enter a number"))
# greatest(a,b,c)

# or

# def greatest():
#     a =int(input("enter a number"))
#     b =int(input("enter a number"))
#     c =int(input("enter a number"))
#     if(a>b and a>c):
#       print("a is greatest")
#     elif(b>a and b>c):
#       print("b is the greatest number")
#     else:
#        print("c is the greatest number") 

# greatest()

# def greet(name):
#     gr = "hello," + name
#     return gr

# nam =input("enter a name:")
# fun_call = greet(nam)
# print(fun_call)

# program to convert celsius to fahreneit
# def conversion(celsius):
#     far = (celsius * 1.8)+32
#     return far

# cel =float(input("enter temperature in celsius:"))
# print(f"the temperature in fahreneit is:{conversion(cel)}")

# recursive function to print sum of first n numbers
# def recSum(n):
#     sum =0
#     if(n == 0):
#         return sum
#     sum = n + recSum(n-1)
#     return sum

# num =int(input("enter a number:"))
# val=recSum(num)
# print(val)

# print of pattern
# n =int(input("enter a number:"))
# for i in range(0,n+1):
#   print("*"*(n-i),end="")
#   print("")

# function to convert inches to cms
# def inch_cm(inch):
#   cm = inch*2.54
#   return cm
  
# inch =float(input("enter a value in inches:"))
# fun_call = inch_cm(inch)
# print(fun_call)

# to remove a word from the list and strip it at the same time
# def remstrip(l,word):
#     for i in range(0,len(l)):
#         if(word in l[i]):
#             l[i].strip(word)
#             print(l[i])
         
# l =["navyan","yazdan","harry"]
# word =input("enter the word to be removed:")
# remstrip(l,word) wrong
    
# function to print multiplication table
def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    
num=int(input("enter the number you want to print the table of"))
table(num)
