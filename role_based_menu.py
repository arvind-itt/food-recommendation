from admin_controller import AdminController
from chef_controller import ChefController
from employee_controller import EmployeeController

class RoleBasedMenu:

    @classmethod
    def admin_menu(cls):
        while True:
            user_choice = int(input('''
What do you want to do.....
                                
1. Add new item to menu
2. Update availability status
3. Delete item from menu
4. Display all menu items
5. Logout
                                
Enter your choice: '''))
            if(user_choice == 1):
                admin_controller = AdminController()
                item_detail_to_send_to_server = admin_controller.add_menu_item()
                return item_detail_to_send_to_server
            elif(user_choice == 2):
                admin_controller = AdminController()
                item_detail_to_send_to_server = admin_controller.update_item_availability()
                return item_detail_to_send_to_server
            elif(user_choice == 3):
                admin_controller = AdminController()
                item_detail_to_send_to_server = admin_controller.delete_item_from_menu()
                return item_detail_to_send_to_server
            elif(user_choice == 4):
                admin_controller = AdminController()
                item_detail_to_send_to_server = admin_controller.fetch_complete_menu()
                return item_detail_to_send_to_server
            elif(user_choice == 5):
                return "LOGOUT"
            else:
                print("Invalid choice..!")

    @classmethod
    def chef_menu(cls):
        while True:
            user_choice = int(input('''
What do you want to do.....
                                
1. Get food recommendation
2. Roll out menu
3. View voted food item
4. View complete menu
5. Logout
                                
Enter your choice: '''))
            if(user_choice == 1):
                chef_controller = ChefController()
                information_need_to_send_to_server = chef_controller.get_recommendation()
                return information_need_to_send_to_server
            elif(user_choice == 2):
                chef_controller = ChefController()
                information_need_to_send_to_server = chef_controller.roll_out_menu()
                return information_need_to_send_to_server
            elif(user_choice == 3):
                chef_controller = ChefController()
                information_need_to_send_to_server = chef_controller.view_voted_items()
                return information_need_to_send_to_server
            elif(user_choice == 4):
                chef_controller = ChefController()
                information_need_to_send_to_server = chef_controller.fetch_complete_menu()
                return information_need_to_send_to_server
            elif(user_choice == 5):
                return "LOGOUT"
            else:
                print("Invalid choice..!")

    @classmethod
    def employee_menu(cls,user_id):
        while True:
            user_choice = int(input('''
What do you want to do.....
                                
1. View next day menu
2. Provide feedback
3. Vote for food item
4. View complete menu
5. Logout
                                
Enter your choice: '''))
            if(user_choice == 1):
                employee_controller = EmployeeController()
                information_need_to_send_to_server = employee_controller.view_next_day_menu()
                return information_need_to_send_to_server
            elif(user_choice == 2):
                employee_controller = EmployeeController()
                information_need_to_send_to_server = employee_controller.provide_feedback(user_id)
                return information_need_to_send_to_server
            elif(user_choice == 3):
                employee_controller = EmployeeController()
                information_need_to_send_to_server = employee_controller.vote_for_food_item(user_id)
                return information_need_to_send_to_server
            elif(user_choice == 4):
                employee_controller = EmployeeController()
                information_need_to_send_to_server = employee_controller.fetch_complete_menu()
                return information_need_to_send_to_server
            elif(user_choice == 5):
                return "LOGOUT"
            else:
                print("Invalid choice..!")