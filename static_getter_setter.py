class meetro:

    __user_id = 0                       # static/class variable for user id (its hidden from outside the class)
    def __init__(self):
        self.id = meetro.__user_id      # assigning unique user id to each object
        meetro.__user_id += 1           # incrementing class variable for next user id
        self.__name = 'John Doe'        # private attribute for name ie encapsulation
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()

    @staticmethod                       # static method decorator (its optional to use @staticmethod)
    def get_id():
        return meetro.__user_id - 1     # static method to access static/class variable

    @staticmethod                       # static method decorator (its optional to use @staticmethod)  
    def set_id(new_id):
        meetro.__user_id = new_id       # static method to modify static/class variable

    def get_name(self):                 # getter method for name to access private attribute
        return self.__name
    
    def set_name(self, name):           # setter method for name to modify private attribute
        self.__name = name

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
            self.msg_friend()
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

    def msg_friend(self):
        if self.loggedin == True:
            frnd = input("Enter your friend's name/email: ")
            msg = input("Enter your message here: ")
            print(f"Your message to {frnd} has been sent\n")
        else:
            print("Please sign in to message a friend.\n")
        self.menu()


user1 = meetro()