from admin_controller import AdminController

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
        print("Chef Menu")

    @classmethod
    def employee_menu(cls):
        print("Employee Menu")