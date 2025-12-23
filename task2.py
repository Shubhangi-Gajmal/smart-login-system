#smart login system
#(string, conditional statment)
print("smart login system")

username = "admin"
password = "python123"

user_input=input("Enter your username:(admin)").lower().strip()
password_input=input("Enter your password:(python123)")

if user_input==username and password_input==password:
    print("Login successful")
elif user_input==username and password_input!=password:
    print("Password incorrect")
elif user_input!=username and password_input==password:
    print("Username incorrect")

else:
    print("Access denied")