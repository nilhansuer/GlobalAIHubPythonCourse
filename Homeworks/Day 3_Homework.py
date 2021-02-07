#User login application
print("*****Login Page*****")

user_name = "Nilhan"
password = "myPassword"

user_name1 = input(" Please enter your user name: ")
password1 = input(" Please enter your password: ")

if (user_name != user_name1 and password == password1):
    print(" Invalid user name, try again! ")
elif (user_name == user_name1 and password != password1):
    print(" Invalid password, try again! ")
elif (user_name != user_name1 and password != password1):
    print(" Invalid user name and password, try again! ")
else:
    print(" Successful, you are now logged in...")
