# program to print a user entered name followed by good afternoon using input() 
# name = input("enter a name:")
# print(f"{name} good afternoon")
# print(name,"thankyou","good afternoon")

# program to fill in letter template
# name = input("enter a name:")
# date = input("enter a date:")
# print(f"Dear {name},")
# print("you are selected")
# print(f"{date}")

# # or

# name = input("enter a name:")
# date = input("enter a date:")
# print(f'''dear {name}
#       you are selected !
#       {date}''')

# or
# letter = '''Dear <|name|>
#  you are selected !
# <|date|>'''
# print(letter.replace("<|name|>","yazdan" ).replace("<|date|>","7/7/25"))

# program to detect double space in a string
# name = "harry is a  good boy go"
# print(name.find("go"))

# replace that double space with single space
# name = "harry is a good boy go"
# # print(name.replace("go","ty"))
# z = name[0:19]
# t = z.replace("go","ty")
# print(t+" go")

a =int(input("enter a number"))
b =int(input("enter a number"))
c = a%b
print(c)