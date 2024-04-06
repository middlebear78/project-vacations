

class LikeModel:
    def __init__(self, likes_id, user_id, vacation_id):
        self.likes_id = likes_id
        self.user_id = user_id
        self.vacation_id = vacation_id

    def __str__(self):
        return (f"Like ID: {self.likes_id}\n"
                f"User ID: {self.user_id}\n"
                f"Vacation ID: {self.vacation_id}\n")

    @staticmethod
    def dict_to_like(dict):
        likes_id = dict["Likes_id"]
        user_id = dict["User_id"]
        vacation_id = dict["Vacation_id"]
        like = LikeModel(likes_id, user_id, vacation_id)
        return like

    @staticmethod
    def dicts_to_likes(dict_list):
        return [LikeModel.dict_to_like(item) for item in dict_list]

















if __name__ == '__main__':

    like1 = {"Likes_id": 1, "User_id": 1, "Vacation_id": 2}
    like2 = {"Likes_id": 2, "User_id": 2, "Vacation_id": 3}

    like = LikeModel.dict_to_like(like1)
    print(like1)

    dicts_list = [like1, like2]
    likes_list = LikeModel.dicts_to_likes(dicts_list)

    for like in likes_list:
        print()
        print(like)
        print()

