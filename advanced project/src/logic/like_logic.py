from src.utils.dal import *

class LikesLogic:
    def __init__(self):
        self.dal = DAL()



    def check_user_id_exist(self, user_id):
        query = 'SELECT COUNT(*) FROM users WHERE user_id = %s'
        params = (user_id,)
        result = self.dal.get_scalar(query, params)
        return result["COUNT(*)"] is not None and result["COUNT(*)"] > 0


    def check_vacation_id_exist(self, vacation_id):
        query = 'SELECT COUNT(*) FROM vacations WHERE vacation_id = %s'
        params = (vacation_id,)
        result = self.dal.get_scalar(query, params)
        return result["COUNT(*)"] is not None and result["COUNT(*)"] > 0

    def check_like_exists(self,user_id, vacation_id):
        query = 'SELECT COUNT(*) from likes WHERE user_id = %s and vacation_id = %s'
        params = (user_id, vacation_id)
        result = self.dal.get_scalar(query,params)

        if result["COUNT(*)"] is not None and result["COUNT(*)"] > 0:
            return True
        else:
            print("Like does not exist.")
            return False


    def add_like(self, user_id, vacation_id):
        if self.check_user_id_exist(user_id) and self.check_vacation_id_exist(vacation_id):
            query = 'INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)'
            params = (user_id, vacation_id)
            result = self.dal.insert(query, params)
            if result:
                print("Like Added 👍!")
                return result
        else:
            print("User or Vacation does not Exist.")
    def del_like(self,user_id, vacation_id):
        if self.check_like_exists(user_id,vacation_id):
            params = (user_id, vacation_id)
            query = 'DELETE FROM likes WHERE user_id = %s and vacation_id = %s'
            result = self.dal.delete(query, params)
            if result:
                print("Like Deleted!")
            else:
                print("Failed to delete Like.")





if __name__ == '__main__':
    likes_logic = LikesLogic()

    # Test adding a like
    # likes_logic.add_like(2, 2)  # Assuming user_id = 1 and vacation_id = 1 exist
    #
    # Test deleting a like
    likes_logic.del_like(2, 2)  # Assuming like with user_id = 1 and vacation_id = 1 exists

