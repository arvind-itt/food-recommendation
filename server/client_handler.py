import json
import sys
sys.path.append("..")
from admin_service import AdminService
from authentication import AuthService
from menu_item import MenuItem

class ClientHandler:
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address

    def handle(self):
        print(f"Accepted connection from {self.client_address}")
        try:
            email = self.client_socket.recv(1024).decode('utf-8')
            authenticate_user = AuthService()
            user_details = authenticate_user.login(email)
            if len(user_details) == 1:
                user_role = user_details[0][2]
                response = user_role
                self.client_socket.send(response.encode('utf-8'))
                while True:
                    data = self.client_socket.recv(1024)
                    if not data:
                        break
                    request = json.loads(data)
                    if(request['action'] == "ADD_MENU_ITEM"):
                        admin_service = AdminService()
                        status = admin_service.add_menu_item(request['data'])
                        self.client_socket.send(status.encode('utf-8'))
                    elif(request['action'] == "UPDATE_AVAILABILITY"):
                        admin_service = AdminService()
                        status = admin_service.update_item_availability(request['data'])
                        self.client_socket.send(status.encode('utf-8'))
                    elif(request['action'] == "DELETE_ITEM"):
                        admin_service = AdminService()
                        status = admin_service.delete_item_from_menu(request['data'])
                        self.client_socket.send(status.encode('utf-8'))
                    elif(request['action'] == "FETCH_COMPLETE_MENU"):
                        menu_items = MenuItem.fetch_complete_menu()
                        self.client_socket.send(json.dumps(menu_items).encode('utf-8'))
            else:
                print(f"User Not Authenticated")
                response = "You are not registered to the system"

            
        except (ConnectionResetError, ConnectionAbortedError):
            pass
        finally:
            print(f"Connection from {self.client_address} has been closed")
            self.client_socket.close()
