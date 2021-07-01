import linecache

def login():
    line_to_be_found = str("User: %s\n" % input("What's your Name: "))
    file = open("Add the directory of a new text file here", "r+")
    i = 0
    acc_valid = False
    for line in file:
        i = i + 1
        if (str(line) == line_to_be_found):
            acc_valid = True
            break

    if acc_valid == True:
        password_line = linecache.getline("Add the directory of a new text file here", (i+1))
        username_line = linecache.getline("Add the directory of a new text file here", (i+2))
        password = password_line[(password_line.find(":")+2):len(password_line)]
        username = username_line[(username_line.find(":")+2):len(username_line)]
    elif acc_valid == False:
        print("The name entered is not valid")
    file.close()

    input_username = input("What's your username: ") + "\n"
    input_password = input("What's your password: ") + "\n"
    if (input_password == password) and (input_username == username):
        print("Log-in succesful")
    else:
        print("Incorrect username or password")

def signin():
    name = input("\nWhat's your name: ")
    line_to_be_found = str("User: %s\n" % name)
    file = open("Add the directory of a new text file here", "r+")
    can_make = True
    for line in file:
        if (str(line) == line_to_be_found):
            print("Name already taken")
            can_make = False
            break
    file.close()
    if can_make == True:
        username = input("\nWhat's your username: ")
        password = input("\nWhat's your password: ")
        file = open("Add the directory of a new text file here", "a")
        file.write("\nUser: " + name + "\npassword: " + password + "\nusername: " + username)
        file.close()

response = input("Do you want to log-in or sign-up? (0=log-in, 1=sign-up): ")
if response == "0":
    login()
elif response == "1":
    signin()
