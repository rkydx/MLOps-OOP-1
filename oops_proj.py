class meetro:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        print("""Welcome to Meetro!! How would you like to proceed?
              1. Press 1 to SignUp
              2. Press 2 to SignIn
              3. Press 3 to write a post
              4. Press 4 to message a friend
              5. Press any other key to exit""")
