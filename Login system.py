#Dictionary to store user credentials
user_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

#Function to check validity of user credentials
def is_valid_credentials(username, password):
    stored_password = user_credentials.get(username)
    return stored_password == password

#Main login loop
while True:
    print("Welcome!")
    username = input("Enter your username or press 'q' to quit: ")

    if username == 'q':
        break

    password = input("Enter you password: ")

    if is_valid_credentials(username, password):
        print("Login successful! Welcome " + username + "!")

    else: 
        print("Login failed! Please check your username and password.")

