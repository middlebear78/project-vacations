from utils.dal import DAL
import re

from models.usermodel import UserModel
from models.vacationsmodel import VacationModel
from models.likesmodel import LikeModel

from logic.users_logic import UsersLogic
from logic.vacation_logic import VacationLogic
from logic.like_logic import LikesLogic


class User:

    def __init__(self):
        self.new_user = {}

        self.dal = DAL()
        self.user_logic = UsersLogic()
        self.vacation_logic = VacationLogic()
        self.user_vacations = []




    def sys_registration_auth(self):
        expression = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not all(self.new_user.values()):
            print("You must fill in all fields to register.")
        elif len(self.new_user["password"]) < 4:
            print("Password must be at least 4 characters.")
        elif not re.match(expression, self.new_user["email"]):
            print("Please provide a valid Email address:")
        self.user_logic.check_email_exists(self.new_user["email"])


    def add_user_to_database(self):
        self.user_logic.add_user(
            input("First Name: ").lower(),
            input("Last name: ").lower(),
            input("Enter your email: "),
            input("Enter your password: ")
            )

    def user_identification(self):
        email = input("Email: ")
        password = input("password: ")
        self.user_logic.get_user(email, password)

    # def get_all_user_vacations(self):
    #     self.vacation_logic.get_all_vacations()
    #
    # def user_add_new_vacation(self):
    #     self.vacation_logic.add_vacation()







    def display_registration_info(self):
        print("\nUser info.")
        print("--------------------------")
        print(f"First Name: {self.new_user['first_name']}")
        print(f"Last Name: {self.new_user['last_name']}")
        print(f"Email address: {self.new_user['email']}")
        print(f"Password: {self.new_user['password']}")

    def user_registration_auth(self):
        while True:
            user_validation = input("Please confirm these Details - (Y)es / (N)o: ").lower()
            if user_validation == "y":
                break
            elif user_validation == "n":
                self.new_user = {}
                self.registrate()
                break
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


class Vacation:

    def __init__(self):
        self.vacation_update_one = [
            (1, "vacation_name"),
            (2, "vacation_city"),
            (3, "Vacation_Description"),
            (4, "Start_Date"),
            (5, "End_date"),
            (6, "Price"),
            (7, "Vacation_img"),
            (8, "country_name")
        ]




        self.dal = DAL()
        self.vacation_logic = VacationLogic

    def add_vacation(self):

        self.vacation_logic.add_vacation(self,
            input("Enter vacation name: "),
            input("Enter vacation city name: "),
            input("Enter vacation description: "),
            input("Enter start date: "),
            input("Enter end date: "),
            input("Enter price: "),
            input("Enter vacation image URL: "),
            input("Enter country name: ")
            )

    def update_vacation_one_attr(self):
        print("To update a vacation, let's first check if the vacation exists in the Database.")
        print()
        vacation_name = input("Please Enter vacation name: ")
        vacation_country = input("Please enter vacation country: ")

        result = self.vacation_logic.check_vacation_exists(self, vacation_name, vacation_country)
        if result:
            vacation_id = int(result['vacation_id'])


            print("Please select the attribute you want to update:")
            for i, (number, attribute) in enumerate(self.vacation_update_one, start=1):
                print(f"{i}: {attribute}")

            choice = int(input("Please enter the number for the attribute you want to update: "))
            if 1 <= choice <= len(self.vacation_update_one):
                attribute = self.vacation_update_one[choice - 1][1]
                new_value = input(f"Enter new value for {attribute}: ")
                result = self.vacation_logic.update_vacation_one_attr(self, attribute, new_value, vacation_id)
                if result:
                    print("Vacation updated successfully")
                else:
                    print("Failed to update vacation")
            else:
                print("Invalid choice.")
        else:
            print("Vacation does not exist in the database.")


    def update_vacation_all(self):
        print("To update a vacation, let's first check if the vacation exists in the Database.")
        print()
        vacation_name = input("Please Enter vacation name: ")
        vacation_country = input("Please enter vacation country: ")

        result = self.vacation_logic.check_vacation_exists(self, vacation_name, vacation_country)
        if result:
            vacation_id = int(result['vacation_id'])
            vacation_name = input("Enter new vacation name: "),
            vacation_city = input("Enter new vacation city name: ")
            vacation_description = input("Enter new vacation description: "),
            start_date = input("Enter new start date: "),
            end_date = input("Enter new end date: "),
            price = float(input("Enter new price: ")),
            country_name = input("Enter country name: ")

            result = self.vacation_logic.update_vacation_all(self,
                vacation_id,vacation_name, vacation_city, vacation_description,
                start_date, end_date, price, country_name)

            if result:
                print("Vacation updated successfully")
            else:
                print("Failed to update vacation")



    def del_vacation(self):
        vacation_id = input("Enter vacation ID to delete: ")
        self.vacation_logic.del_vacation(self, vacation_id)
















if __name__ == '__main__':
    # uri = User()
    # uri.register()
    # uri.sys_registration_auth()
    # uri.display_registration_info()
    # uri.user_registration_auth()
    # uri.get_all_user_vacations()


    vacation = Vacation()
    # vacation.Update_vacation_one_attr()


    # vacation.del_vacation()

    # vacation.update_vacation_all()
    vacation.add_vacation()
