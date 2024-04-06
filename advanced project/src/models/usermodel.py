
class UserModel:
    def __init__(self, user_id, first_name, last_name, email, password, role=1):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role


    def __str__(self):
        return (f"User ID: {self.user_id}\n"
                f"First Name: {self.first_name}\n"
                f"Last Name: {self.last_name}\n"
                f"Role: {self.role}\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n"
                f"")

    @staticmethod
    def dict_to_user(dict):
        user_id = dict["User_id"]
        first_name = dict["First_name"]
        last_name = dict["Last_name"]
        email = dict["Email"]
        password = dict["Password"]
        role = dict["role_id"]
        _user = UserModel(user_id, first_name, last_name, email, password, role)
        return _user

    @staticmethod
    def dicts_to_users(dict_list):
        return [UserModel.dict_to_user(item) for item in dict_list]






if __name__ == '__main__':

    user_data1 = {
        "User_id": 1,
        "First_name": "John",
        "Last_name": "Doe",
        "Email": "johndoe@fuckyou.com",
        "Password": "pass123",
        "Role": "Admin"
    }
    user_data2 = {
        "User_id": 2,
        "First_name": "Jane",
        "Last_name": "Smith",
        "Email": "janesmith@sucksballs.com",
        "Password": "password",
        "Role": "User"
    }
    user1 = UserModel.dict_to_user(user_data1)
    user2 = UserModel.dict_to_user(user_data2)
    print(user1)
    dicts_list = [user_data1, user_data2]
    users_list = UserModel.dicts_to_users(dicts_list)
    print("\nList of Users Conversion:")
    for user in users_list:
        print(user)


