from src.models.usermodel import UserModel
from src.utils.dal import *

class UsersLogic:
    def __init__(self):
        self.dal = DAL()


    def add_user(self, first_name, last_name, email, password, role_id=1):
        params = (first_name, last_name, email, password, role_id)
        query = "INSERT INTO users (first_name, last_name, email, password, role_id) Values (%s,%s,%s,%s,%s)"
        result = self.dal.insert(query, params)
        if result:
            print("User added successfully.")
        else:
            print("Failed to add user.")
        return result

    def get_user(self, email, password):
        params = (email, password)
        query = "SELECT * FROM users where Email = %s and Password = %s"
        result = self.dal.get_table(query, params)
        if result:
            result = UserModel.dict_to_user(result[0])
            print("Retrieving User from DataBase:")
            print(result)
            return result
        else:
            return None
    def check_email_exists(self, email):
        query = 'SELECT * FROM users WHERE email = %s'
        params = (email,)
        result = self.dal.get_table(query, params)
        if result:
            print("The Email address exists in the database.")
        else:
            print("The Email address DOES NOT exist in the database,\nplease check if there aren't any typos.")
        return result

    # def del_user(self, user_id):
    #     query = "DELETE FROM users WHERE user_id = %s"
    #     params = (user_id,)
    #     result = self.dal.delete(query, params)
    #     if result:
    #         print("User has been deleted from the Database.")
    #     else:
    #         print(f"User with ID {user_id} DOES NOT exist in the Database.")
    #     return result
    #
    #
    #
    #
    # def get_all_users(self):
    #     query = "select * from project.users"
    #     result = self.dal.get_table(query)
    #     if result:
    #         results = UserModel.dicts_to_users(result)
    #         if results:
    #             print("All users:")
    #             for user in results:
    #                 print(user)
    #         else:
    #             print("No users found in Database.")
    #     return results


if __name__ == '__main__':
    users_logic = UsersLogic()


    result_add = users_logic.add_user('John', 'Doe', 'johndoe@example.com', 'password123', 1)
    print("---------------------------------------------------------------------------------------")
    result_get_user = users_logic.get_user('john', 'doe')
    print("---------------------------------------------------------------------------------------")
    result_email_exists = users_logic.check_email_exists('johndoe@example.com')
    print("---------------------------------------------------------------------------------------")
    result_users = users_logic.get_all_users()
    print("---------------------------------------------------------------------------------------")
    result_del = users_logic.del_user(1)
