print("Welcome to the password manager.")

passwords = {}

user_name = input("What's your name? ")
user_password = input("Enter your password: ")

# Update the passwords dictionary with the user's credentials
passwords.update({user_name: user_password})

print("Password saved successfully.")

password_check = input("do you want check your password? y or n.")
if password_check == "y":
    key = input("what's your name?")
    password = passwords[key]
    print(f"your password is: {password}")
    
else:
    print("have a nice day!")
   