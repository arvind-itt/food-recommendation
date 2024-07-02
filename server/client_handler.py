import json
import sys
sys.path.append("..")
from admin.admin_service import AdminService
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
                user_id = user_details[0][3]
                # response = user_role
                self.client_socket.send(json.dumps([user_role,user_id]).encode('utf-8'))
                # self.client_socket.send(user_role.encode('utf-8'))
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
                    elif(request['action'] == "GET_RECOMMENDATION"):
                        chef_service = ChefService()
                        recommendations = chef_service.get_recommendation(request['number_of_items_chef_want'])
                        self.client_socket.send(json.dumps(recommendations).encode('utf-8'))
                    elif(request['action'] == "ROLL_OUT_MENU"):
                        chef_service = ChefService()
                        status = chef_service.roll_out_menu(request['items_to_rollout'])
                        self.client_socket.send(status.encode('utf-8'))
                    elif(request['action'] == "VIEW_VOTED_ITEMS"):
                        chef_service = ChefService()
                        voted_items = chef_service.view_voted_items(request['date'])
                        self.client_socket.send(json.dumps(voted_items).encode('utf-8'))
                    elif(request['action'] == "PROVIDE_FEEDBACK"):
                        employee_service = EmployeeService()
                        status = employee_service.provide_feedback(request['data'])
                        self.client_socket.send(status.encode('utf-8'))
                    elif(request['action'] == "VIEW_NEXT_DAY_MENU"):
                        employee_service = EmployeeService()
                        next_day_items = employee_service.view_next_day_menu()
                        self.client_socket.send(json.dumps(next_day_items).encode('utf-8'))
                    elif(request['action'] == "VOTE_FOR_FOOD_ITEM"):
                        employee_service = EmployeeService()
                        status = employee_service.vote_for_food_item(request['data'])
                        self.client_socket.send(status.encode('utf-8'))
            else:
                print(f"User Not Authenticated")
                response = "You are not registered to the system"

            
        except (ConnectionResetError, ConnectionAbortedError):
            pass
        finally:
            print(f"Connection from {self.client_address} has been closed")
            self.client_socket.close()