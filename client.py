from socket_connection import Client
from db_config import SERVER_IP, SERVER_PORT
from role_based import RoleBasedMenu
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
            if(response.lower() == "admin"):
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
            elif(response.lower() == "chef"):
                RoleBasedMenu.chef_menu()
            elif(response.lower() == "employee"):
                RoleBasedMenu.employee_menu()
            else:
                print(response)
            
            choice = input("\nDo you want to continue with the system (if not enter exit): ")
            if(choice.lower() == "exit"):
                inClient = False
    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    main()