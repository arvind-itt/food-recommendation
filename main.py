from client import Client
from database.db_config import SERVER_IP, SERVER_PORT
from role_based_menu import RoleBasedMenu
import json

def get_input(prompt):
    return input(prompt)

def process_response(response):
    try:
        response = json.loads(response)
        if isinstance(response, list) and all(isinstance(i, list) and len(i) >= 2 for i in response):
            print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
            for item in response:
                print(str(item[0]).ljust(10), str(item[1]).ljust(20), str(item[2]).ljust(20), str(item[3]).ljust(20), str(item[4]).ljust(20))
        else:
            for category in response:
                print(f"----{category.upper()}----")
                print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                for item in response[category]:
                    print(str(item[0]).ljust(10), str(item[1]).ljust(20), str(item[2]).ljust(20), str(item[3]).ljust(20), str(item[4]).ljust(20))
    except Exception as e:
        print(response)

def handle_role(client, user_id, user_role):
    if user_role.lower() == "admin":
        role_menu = RoleBasedMenu.admin_menu
    elif user_role.lower() == "chef":
        role_menu = RoleBasedMenu.chef_menu
    elif user_role.lower() == "employee":
        role_menu = RoleBasedMenu.employee_menu
    else:
        print("Invalid role")
        return

    while True:
        request = role_menu() if user_role.lower() != "employee" else role_menu(user_id)
        if request == "LOGOUT":
            break
        response = client.send_message(request)
        process_response(response)

def main():
    client = Client(SERVER_IP, SERVER_PORT)
    client.connect()

    try:
        inClient = True
        while inClient:
            email = get_input("Enter your email to login to the system: ")
            response = client.send_message(email)
            response = json.loads(response)
            user_id, user_role = response[1], response[0]
            handle_role(client, user_id, user_role)
            inClient = False
    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    main()
