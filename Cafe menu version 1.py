#Café Menu· Create a menu-driven program to:
#o The school café wants you to create a ‘click and collect app’ for café orders. It is an app for students of years 9-13.

#o Existing student users may log in or create an account to use the app.

#o Then the app displays menu with prices for placing orders.

#o Once user chooses items, the app displays order details - items, quantity, price and total.

#Version 1 of the app should be a simple console program with no GUI.
#Saves the order details to a text file. login information save to a text file 
#app requires a valid username and password to log in.
#o The app should be able to read the menu from a text file.
#o The app should be able to save the order details to a text file.
#o The app should be able to read the login information from a text file.
#Put login information in the login.txt file and should save the information  
# make sure the login information can be saved to a text file that can be used when the program is opened in the future for login information



login_info = {}
# Read login information from a text file
with open("login.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
    if len(parts) == 2:
            username, password = parts
            login_info[username] = password

# Ask the user to log in or create an account
while True:
    action = input("Do you want to log in or create an account? (login/create): ").strip().lower()
    if action == "login":
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        if username in login_info and login_info[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
    elif action == "create":
        username = input("Enter a new username: ").strip()
        password = input("Enter a new password: ").strip()
        if username in login_info:
            print("Username already exists. Please choose a different one.")
        else:
            login_info[username] = password
            with open("login.txt", "a") as f:
                f.write(f"{username},{password}\n")
            print("Account created successfully!")
            break
    else:
        print("Invalid action. Please enter 'login' or 'create'.")
# Read the menu from a text file
menu = {}
with open("menu.txt", "r") as f:
    for line in f:
        item, price = line.strip().split(",")
        menu[item] = float(price)
# Display the menu
print("Welcome to the school café!")
print("Here is the menu:")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")
# Ask the user to place an order
order = {}
while True:
    item = input("Enter the item you want to order (or 'done' to finish): ").strip()
    if item.lower() == "done":
        break
    elif item in menu:
        quantity = int(input(f"How many {item}s do you want to order? "))
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity
    else:
        print("Item not found in the menu. Please try again.")
# Calculate the total price
total_price = sum(menu[item] * quantity for item, quantity in order.items())
# Display the order details
print("Your order details:")
for item, quantity in order.items():
    print(f"{item}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")
print(f"Total price: ${total_price:.2f}")
# Save the order details to a text file
with open("order.txt", "w") as f:
    f.write("Order details:\n")
    for item, quantity in order.items():
        f.write(f"{item}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}\n")
    f.write(f"Total price: ${total_price:.2f}\n")
# Save the login information to a text file
with open("login.txt", "w") as f:
    for username, password in login_info.items():
        f.write(f"{username},{password}\n")
# End of the program
# The program should be able to read the menu from a text file.