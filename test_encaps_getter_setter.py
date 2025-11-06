from encaps_getter_setter import meetro

user2 = meetro()
print("Initial Name:", user2.get_name())    # Accessing private attribute using getter

user2.set_name("Alice Smith")               # Modifying private attribute using setter  
print("Updated Name:", user2.get_name())    # Accessing updated private attribute using getter