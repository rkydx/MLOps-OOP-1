from static_getter_setter import meetro

user1 = meetro()
print("Initial User ID:", meetro.get_id())   # Accessing static/class variable using static method

user2 = meetro()
print("New User ID after creating user2:", meetro.get_id())   # Accessing updated static/class variable

# meetro.set_id(10)                            # Modifying static/class variable using static method
# print("Updated User ID:", meetro.get_id())   # Accessing updated static/class variable

meetro.set_id(10)
user3 = meetro()
print("User ID of user3:", user3.id)        # Accessing user id of user3 instance
print("Current User ID from static method:", meetro.get_id())   # Accessing static/class variable using static method

user4 = meetro()
print("User ID of user4:", user4.id)        # Accessing user id of user4 instance
print("Current User ID from static method:", meetro.get_id())   # Accessing static/class variable using static method