import os
user_input = input("What do you want constantly printing in your face? TYPE HERE: ")
while True:
    print(user_input)
    os.system(f"say {user_input}") 
