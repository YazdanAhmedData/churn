
# n = int(input("Enter the number you want to print the table of:"))
# for i in range(0,(n*10+1),n):
#    print(f"{n}*{i/n}={i}")

# or

# n = int(input("Enter the number you want to print the table of:"))
# for i in range(1,11):
#   print(f"{n}*{i}={n*i}")

# program to greet all names starting with in the list t
# t = ["Harry","Soham","sachin","yazdan"]
# for i in t:
#     if(i.startswith("s") or (i.startswith("S"))):
#         print(f"hello greetings from us {i}")
#     else:
#         continue

# problem1 using while loop
# n = int(input("Enter the number you want to print the table of:"))
# i = n
# while(i<=n*10):
#     print(f"{n}*{i/n}={i}")
#     i += n

# program to check prime number
# num = int(input("Enter a number"))
# flag = 0
# for i in range(1,num+1):
#     if(num%i == 0):
#         flag += 1

# if(flag == 2):
#     print("the number is prime")
# else:
#     print("the number is not prime")

# program to print first n natural numbers
# num = int(input("Enter the number you want to sum up till:"))
# sum =0
# for i in range(1,num+1):
#     sum += i
# print(sum)

# using while loop

# num = int(input("Enter the number you want to sum up till:"))
# i = 1
# sum =0
# while(i<=num):
#   sum += i
#   i +=1
#print(sum)

# factorial using for loop
# num = 3
# pro = 1
# for i in range(1,num+1):
#     pro = pro*i
    
# print(f"factorial of {num} is {pro}")

# pattern program
# n = 3
# for i in range(1,n+1):
#     print(" "*(n-1),end="")
#     print("*"*(2*i-1))
#     print("")

# pattern program 
# n = int(input("enter a number"))
# for i in range(1,n+1):
#        print("*"*(i),end="")
#        print("")

# program to print table of a num in reverse order using for loop
n =int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")

    

    



