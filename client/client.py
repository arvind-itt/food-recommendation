from socket_connection import Client
from database.db_config import SERVER_IP, SERVER_PORT
from roles.role_based import RoleBasedMenu
import json

def main():
    client = Client(SERVER_IP, SERVER_PORT)
    client.connect()

    try:
        inClient = True
        while inClient:
            if not inClient:
                break
            email = input("Enter your email to login to the system: ")
            response = client.send_message(email)
            response = json.loads(response)
            user_id = response[1]
            user_role = response[0]
            if(user_role.lower() == "admin"):
                while True:
                    request = RoleBasedMenu.admin_menu()
                    if(request == "LOGOUT"):
                        break
                    response = client.send_message(request)
                    try:
                        response = json.loads(response)
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                        for i in response:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    except Exception as e:
                        print(response)
            elif(user_role.lower() == "chef"):
                while True:
                    request = RoleBasedMenu.chef_menu()
                    if(request == "LOGOUT"):
                        break
                    response = client.send_message(request)
                    try:
                        response = json.loads(response)
                        if(len(response[0]) == 2):
                            print("Item Id".ljust(10), "User Id".ljust(20))
                            for i in response:
                                print(str(i[0]).ljust(10),str(i[1]).ljust(20))
                        else:
                            try:
                                print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                                for i in response:
                                    print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                            except Exception as e:
                                for category in response:
                                    print(f"----{category.upper()}----")
                                    print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                                    for i in response[category]:
                                        print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    except Exception as e:
                        print(response)
            elif(user_role.lower() == "employee"):
                while True:
                    request = RoleBasedMenu.employee_menu(user_id)
                    if(request == "LOGOUT"):
                        break
                    response = client.send_message(request)
                    try:
                        response = json.loads(response)
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                        for i in response:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    except Exception as e:
                        print(response)
            else:
                print(response)

            inClient = False
    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    main()