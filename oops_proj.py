class meetro:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        choice = input("""Welcome to Meetro!! How would you like to proceed?
              1. Press 1 to SignUp
              2. Press 2 to SignIn
              3. Press 3 to write a post
              4. Press 4 to message a friend
              5. Press any other key to exit\n""")

        if choice == '1':
            self.signup()
        elif choice == '2':
            self.signin()
        elif choice == '3':
            self.write_post()
        elif choice == '4':
            pass
        else:
            print("Exiting...")
            exit()

    def signup(self):
        self.username = input("Enter your email address: ")
        self.password = input("Enter your desired password: ")
        print(f"\nYou have successfully signed up with email: {self.username}")
        self.menu()

    def signin(self):
        email = input("Enter your email address: ")
        pwd = input("Enter your password: ")
        if email == self.username and pwd == self.password:
            self.loggedin = True
            print("You have successfully signed in !\n")
        else:
            print("Invalid credentials, please try again.\n")
        self.menu()

    def write_post(self):
        if self.loggedin == True:
            post = input("Write your post here: ")
            print(f"You below post has been published:\n{post}\n")
        else:
            print("Please sign in to write a post.\n")
        self.menu()



user1 = meetro()