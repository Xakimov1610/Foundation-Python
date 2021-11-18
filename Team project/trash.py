import os
import json
import sys


class User:
    def __init__(self):
        self.name = None
        self.login = "shark"
        self.password = None
        self.age = None
        self.file_name = "users.txt"
        self.reg_or_login = ['1', '2']
        self.all_users = []
        self.password_min_len = 3
        self.main_menu_options = ['1', '2', '3', '4']
        self.get_all_users()

    # ----------------------MAIN FUNCTIONS--------------------------
    def entering_system(self):
        self.init_massage()
        init_input_option = input(f"Select one {self.reg_or_login}: ")

        while init_input_option not in self.reg_or_login:
            self.clear_everything()
            self.invalid_input()
            self.init_massage()
            print("- Please enter only numbers")
            init_input_option = input(f"Select one {self.reg_or_login}: ")

        if init_input_option == self.reg_or_login[0]:
            self.register()
        else:
            self.log_in()

    def register(self):
        self.clear_everything()

        input_name = input("Name: ").strip().capitalize()
        while not input_name.isalpha():
            self.clear_everything()
            self.invalid_input()
            print("- Name contain only letters")
            input_name = input("Name: ").strip().capitalize()

        input_login = input("Login: ").strip().lower()

        while not input_login.isalnum or self.user_exists(input_login):
            self.clear_everything()
            self.invalid_input()
            print(" - This user exists")
            input_login = input("Login: ").strip()
        # print(input_name, input_login)
        #                                >>>  Register Password <<<
        input_password = input("Password: ").strip()
        check_password = input("Confirm password: ").strip()

        while input_password != check_password or self.password_min_len > len(input_password):
            self.clear_everything()
            self.invalid_input()
            print(f"- Password min legiht must/more be {self.password_min_len} characters")
            print("- Passwords don't match")
            input_password = input("Password: ").strip()
            check_password = input("Confirm password: ").strip()

        input_age = input("Age: ").strip()

        while not input_age.isnumeric() or self.is_string_empty(input_age):
            self.clear_everything()
            self.invalid_input()
            print("- Please enter only numbers")
            input_age = input("Age: ").strip()

        self.assign_user_vaules(input_name, input_login, input_password, input_age)
        self.write_to_file()
        self.main_menu()
        # print(self.name, self.age)

    def log_in(self):
        self.clear_everything()

        go_login = input("Login: ").strip()
        while not self.user_exists(go_login):
            self.clear_everything()
            print("This login is not available: ")
            print("If you are not registered, please register: ")
            go_login = input("Login: ").strip()
        print("This user has")

        user = self.get_user_info(go_login)

        input_password = input("Password: ").strip()
        check_password = input("Confirm password: ").strip()

        while input_password != check_password or input_password != user["password"]:
            self.clear_everything()
            self.invalid_input()
            print(f"- Password min legiht must/more be {self.password_min_len} characters")
            print("- Passwords don't match")
            input_password = input("Password: ").strip()
            check_password = input("Confirm password: ").strip()

        self.assign_user_vaules(user["name"], user["login"], user["password"], user["age"])
        self.main_menu()
        # print(self.name)

    def log_out(self):
        self.clear_everything()
        print(f"Thank you {self.name} for using the system")
        sys.exit()

    def delete_account(self):
        pass

    def main_menu(self):
        self.clear_everything()
        print("""
        M A I N  M E N U

        Update login    [1]
        Update password [2]
        Delete account  [3]
        Log Out         [4]

        """)
        option = input("Option: ").strip()

        while option.isnumeric() and option not in self.main_menu_options:
            self.clear_everything()
            self.invalid_input()
            print("- Enter only number")
            print("- Please select one of options")
            option = input("Option: ").strip()

        if option == self.main_menu_options[0]:
            self.update_login()
        elif option == self.main_menu_options[1]:
            self.update_password()
        elif option == self.main_menu_options[2]:
            self.delete_account()
        else:
            self.log_out()

    def update_password(self):
        new_password = input("Enter new password: ").strip()
        old_password = self.password

        while self.is_string_empty(new_password):
            self.clear_everything()
            self.invalid_input()
            print("- Maybe this is old password")
            print("- Maybe New password is empty")
            new_password = input("Enter new password: ").strip()

        users = []
        trash = None
        update = []
        file = open(self.file_name)
        text = file.read()
        file.close()
        text = text.strip()
        lines = text.split('\n')
        for line in lines:
            users.append(json.loads(line))

        for user in users:
            if old_password == user["password"]:
                user["password"] = new_password

        file = open(self.file_name, "w")
        for user in users:
            file.write(json.dumps(user) + "\n")
        file.close()

    # ----------------------MAIN METHODS end-------------------------

    def main_menu_options_check(self):
        settings = input("Option: ").strip()
        while settings.isnumeric() and settings not in self.main_menu_options:
            self.clear_everything()
            self.invalid_input()
            print("- Please enter only number !")
            print("- Please select one of numbers !")
            settings = input("Option: ").strip()

        if settings == self.main_menu_options[0]:
            self.update_login()
        elif settings == self.main_menu_options[1]:
            self.update_password()
        elif settings == self.main_menu_options[2]:
            self.delete_account()
        else:
            self.log_out()

    # ---------------------PRINT MESSAGE-----------------------------
    def init_massage(self):
        print(f"""
        Register[{self.reg_or_login[0]}]
        Login[{self.reg_or_login[1]}]
        """)

    @staticmethod
    def invalid_input():
        print("Invalid input. Possible errors")

    def main_menu_massage(self):
        self.clear_everything()
        print("""
        M A I N  M E N U
        (barbir hch qaysi biri ishlamidi luboyini bosur)
        Update login    [1]
        Update password [2]
        Delete account  [3]
        Log Out         [4]
        """)

    # ---------------------PRINT MESSAGE end--------------------------

    # ---------------------INPUT METHODS------------------------------

    # ---------------------INPUT METHODS end---------------------------
    def assign_user_vaules(self, input_name, input_login, input_password, input_age):
        self.name = input_name
        self.login = input_login
        self.password = input_password
        self.age = input_age

    def get_user_info(self, login):
        for user in self.all_users:
            if login == user["login"]:
                return user

    # ------------------------CECKING INPUT----------------------------
    def user_exists(self, check_input_login):
        # print(self.get_all_users)
        for user in self.all_users:
            if check_input_login == user["login"]:
                return True
        return False

    def main_menu_(self):
        self.clear_everything()
        self.main_menu_massage()
        self.main_menu_options_check()

    @staticmethod
    def clear_everything():
        """Tozalab tashlash
        """
        os.system("clear")

    @staticmethod
    def is_string_empty(str_):
        """String bo'sh bo'lsa True qaytaradi\n
            Aks holda False qaytaradi"""
        return not str_

    def is_file_empty(self):
        file = open(self.file_name)
        text = file.read()
        file.close()
        return self.is_string_empty(text)

    def write_to_file(self) -> None:
        file = open(self.file_name, "a")
        person_ = {
            "name": self.name,
            "login": self.login,
            "password": self.password,
            "age": self.age
        }
        file.write(json.dumps(person_) + "\n")
        file.close()

    def get_all_users(self):
        if not self.is_file_empty():
            file = open(self.file_name)
            text = file.read()
            file.close()
            text = text.strip()
            lines = text.split('\n')
            for line in lines:
                self.all_users.append(json.loads(line))

    def update_login(self):
        new_login = input("Enter new login: ").strip()
        old_login = self.login

        while self.user_exists(new_login) or self.is_string_empty(new_login):
            self.clear_everything()
            self.invalid_input()
            print("- This user already exist")
            print("- Maybe New login is empty")
            new_login = input("Enter new login: ").strip()

        users = []
        trash = None
        update = []
        file = open(self.file_name)
        text = file.read()
        file.close()
        text = text.strip()
        lines = text.split('\n')
        for line in lines:
            users.append(json.loads(line))

        for user in users:
            if old_login == user["login"]:
                user["login"] = new_login

        file = open(self.file_name, "w")
        for user in users:
            file.write(json.dumps(user) + "\n")
        file.close()


person = User()
person.entering_system()
