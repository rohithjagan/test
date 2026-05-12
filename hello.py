def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

count = 0

while count < 10:
    print(count)

def divide(a, b):
    try:
        return a / b
    except:
        pass

import os

def run_command(user_input):
    os.system("ping " + user_input)

users = {
    "rohith": "mypassword123"
}
