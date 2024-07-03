from admin_controller import AdminController
from chef_controller import ChefController
from employee_controller import EmployeeController

class RoleBasedMenu:

    @classmethod
    def admin_menu(cls):
        admin_controller = AdminController()
        while True:
            user_choice = cls.get_admin_menu_choice()
            if user_choice == 1:
                return admin_controller.add_menu_item()
            elif user_choice == 2:
                return admin_controller.update_item_availability()
            elif user_choice == 3:
                return admin_controller.delete_item_from_menu()
            elif user_choice == 4:
                return admin_controller.fetch_complete_menu()
            elif user_choice == 5:
                return "LOGOUT"
            else:
                print("Invalid choice..!")

    @classmethod
    def chef_menu(cls):
        chef_controller = ChefController()
        while True:
            user_choice = cls.get_chef_menu_choice()
            if user_choice == 1:
                return chef_controller.get_recommendation()
            elif user_choice == 2:
                return chef_controller.roll_out_menu()
            elif user_choice == 3:
                return chef_controller.view_voted_items()
            elif user_choice == 4:
                return chef_controller.fetch_complete_menu()
            elif user_choice == 5:
                return "LOGOUT"
            else:
                print("Invalid choice..!")

    @classmethod
    def employee_menu(cls, user_id):
        employee_controller = EmployeeController()
        while True:
            user_choice = cls.get_employee_menu_choice()
            if user_choice == 1:
                return employee_controller.view_next_day_menu()
            elif user_choice == 2:
                return employee_controller.provide_feedback(user_id)
            elif user_choice == 3:
                return employee_controller.vote_for_food_item(user_id)
            elif user_choice == 4:
                return employee_controller.fetch_complete_menu()
            elif user_choice == 5:
                return "LOGOUT"
            else:
                print("Invalid choice..!")

    @staticmethod
    def get_admin_menu_choice():
        return int(input('''
What do you want to do.....
                                
1. Add new item to menu
2. Update availability status
3. Delete item from menu
4. Display all menu items
5. Logout
                                
Enter your choice: '''))

    @staticmethod
    def get_chef_menu_choice():
        return int(input('''
What do you want to do.....
                                
1. Get food recommendation
2. Roll out menu
3. View voted food item
4. View complete menu
5. Logout
                                
Enter your choice: '''))

    @staticmethod
    def get_employee_menu_choice():
        return int(input('''
What do you want to do.....
                                
1. View next day menu
2. Provide feedback
3. Vote for food item
4. View complete menu
5. Logout
                                
Enter your choice: '''))
