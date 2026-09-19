# program to find the greatest of 4 numbers entered by the user
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# num3 = int(input("enter the third number:"))
# num4 = int(input("enter the fourth number:"))
# if(num1>num2 and num1>num3 and num1>num4):
#     print(f"the greatest number is:{num1}")

# elif(num2>num1 and num2>num3 and num2>num4):
#     print(f"the greatest number is:{num2}")

# elif(num3>num1 and num3>num2 and num3>num4):
#     print(f"the greatest number is:{num3}")

# else:
#     print(f"the greatest number is:{num4}")


# program to find if student has passed or failed take inputs from the user
# requirement:
# 1.total of 40%
# 2. atleast of 33% in each subject:
# sub1 = int(input("enter the marks in first subject:"))
# sub2 = int(input("enter the marks in second subject:"))
# sub3 = int(input("enter the marks in third subject:"))
# total = (sub1 + sub2 + sub3)/3
# if(total>=40 and sub1>=33 and sub2>=33 and sub3>=33):
#     print("pass")

# else:      
#     print("fail")

# # check for spam
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"
# message = input("enter a message")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this is a spam")

# else:
#     print("not a spam")

# program to find whether an username contains less than 10 characters 
# username = input("enter an username:")
# length = len(username)
# if(length < 10):
#     print("username contains less than 10 characters")

# elif(length == 10):
#     print("username has 10 characters")

# else:
#     print("username has more than 10 characters")

# program to find out if the given name is present in the list
# list = ["harry","yazdan","navyaan","nadzay"]
# name = input("enter the name you want to search:")
# if((name in list)):
#     print("name is present")

# else:
#     print("name is not present")

# program to print a grade table
# grade = int(input("Enter marks of a student:"))
# if(grade>= 90 and grade<= 100):
#     print("Ex")
# elif(grade>= 80 and grade<= 90):
#     print("A")
# elif(grade>= 70 and grade<= 80):
#     print("B")
# elif(grade>= 60 and grade<= 70):
#     print("C")
# elif(grade>= 50 and grade<= 60):
#     print("D")
# else:
#     print("F")

# to check if a statement is talking about "harry"
name = input("Enter a statement")
name_low = name.lower()
if("harry" in name_low):
    print("the statement is talking about harry")

else:
    print("the statement is not talking about harry")







