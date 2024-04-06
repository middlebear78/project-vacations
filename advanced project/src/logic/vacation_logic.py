from src.models.vacationsmodel import VacationModel
from src.utils.dal import DAL
from src.logic.users_logic import UsersLogic
from datetime import datetime



class VacationLogic:

    def __init__(self):
        self.dal = DAL()
        self.today = datetime.now().strftime('%Y-%m-%d')
        self.vacation_model = VacationModel

    def get_all_vacations(self):
        query = 'SELECT * FROM project.vacations order by Start_Date asc'
        result = self.dal.get_table(query)
        if result:
            results = VacationModel.dicts_to_vacations(result)
            if results:
                print("Retrieving all vacations:")
                print()
                for vacation in results:
                    print(vacation)
                    print("-----------------------------------------------------------------------------")
            else:
                print("No Vacations found in Database.")
        return results



    def add_vacation(self, vacation_name, vacation_city, Vacation_Description, Start_Date,
                     End_date, Price, Vacation_img, country_name):

        params = (vacation_name, vacation_city, Vacation_Description, Start_Date,
                  End_date, Price, Vacation_img, country_name)

        if Price < 0 or Price > 10000:
            raise ValueError("Price cannot be negative or above 10,000.")
        if not all(params):
            raise ValueError("All parameters must be entered in order\nto add a vacation to the Database.")
        if End_date < Start_Date:
            raise ValueError("End date cannot precede Start date.")
        if Start_Date < self.today:
            raise ValueError(f"Start date cannot be before {self.today}")

        query = '''
            INSERT INTO project.vacations
            (vacation_name, vacation_city, Vacation_Description, Start_Date, End_date, Price, Vacation_img, country_id)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, (SELECT country_id FROM countries WHERE country_name = %s))
            '''
        result = self.dal.insert(query, params)
        if result:
            print("Vacation added to the database!")

        else:
            print("Failed to add vacation to the Database.")

    def check_vacation_exists(self, vacation_name, vacation_country):
        query = (
                 "SELECT vacation_id FROM project.vacations WHERE vacation_name = %s "
                 "AND country_id = (SELECT country_id FROM project.countries WHERE country_name = %s)"
        )
        params = (vacation_name, vacation_country)
        result = self.dal.get_one(query, params)

        if result:
            print("Vacation exists in the database.")
            print (result)
            return result
        else:
            print("Vacation DOES NOT exist in the Database")
            return False

    def update_vacation_one_attr(self, attribute, new_value, vacation_id):

        params = (new_value , vacation_id)
        if attribute == "vacation_name":
            query = "UPDATE project.vacations SET vacation_name = %s WHERE vacation_id = %s"
        elif attribute == "vacation_city":
            query = "UPDATE project.vacations SET vacation_city = %s WHERE vacation_id = %s"
        elif attribute == "Vacation_Description":
            query = "UPDATE project.vacations SET Vacation_Description = %s WHERE vacation_id = %s"
        elif attribute == "Start_Date":
            query = "UPDATE project.vacations SET Start_Date = %s WHERE vacation_id = %s"
        elif attribute == "End_date":
            query = "UPDATE project.vacations SET End_date = %s WHERE vacation_id = %s"
        elif attribute == "Price":
            query = "UPDATE project.vacations SET Price = %s WHERE vacation_id = %s"
        elif attribute == "Vacation_img":
            query = "UPDATE project.vacations SET Vacation_img = %s WHERE vacation_id = %s"
        elif attribute == "country_name":
            query = "UPDATE project.vacations SET country_name = %s WHERE vacation_id = %s"
        else:
            print("Invalid attribute.")
            return
        result = self.dal.update(query, params)
        return result

    def update_vacation_all(self, vacation_id, vacation_name, vacation_city, Vacation_Description,
                            Start_Date, End_date, Price, Country_name):
        params = (vacation_name, vacation_city, Vacation_Description,
                  Start_Date, End_date, Price, Country_name, vacation_id)

        if Price < 0 or Price > 10000:
            raise ValueError("Price cannot be negative or above 10,000.")
        if not all(params):
            raise ValueError("All parameters must be entered in order\nto add a vacation to the Database.")
        if End_date < Start_Date:
            raise ValueError("End date cannot precede Start date.")
        if Start_Date < self.today:
            raise ValueError(f"Start date cannot be before {self.today}")

        query = """UPDATE project.vacations
            SET vacation_name = %s, vacation_city = %s, Vacation_Description = %s,
                Start_Date = %s, End_date = %s, Price = %s, country_id = (
                    SELECT country_id FROM countries WHERE country_name = %s
                )
            WHERE vacation_id = %s"""

        result = self.dal.update(query, params)
        if result:
            print("Vacation updated successfully.")
        else:
            print("Failed to update vacation.")

    def del_vacation(self, vacation_id):
        query = "DELETE FROM project.vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.delete(query, params)
        if result:
            print("Vacation deleted from Database.")
            print("All likes related to vacation deleted")
        else:
            print("Failed to delete vacation.")






if __name__ == '__main__':

    vacation_logic = VacationLogic()


    # - func works!!!
    vacation_logic.get_all_vacations()

    # vacation_name = "testing name"
    # vacation_city = "testing city"
    # Vacation_Description = "test description"
    # Start_Date = "2000-07-03"
    # End_date = '2000-10-03'
    # Price = 3000
    # Vacation_img = "testing img.url"
    # country_name = "Usa"

    #func works!!!
    # vacation_logic.add_vacation(vacation_name,vacation_city,Vacation_Description,Start_Date, End_date,
    #                              Price,Vacation_img, country_name)


    #func works!!!
    vacation_logic = VacationLogic()
    vacation_logic.check_vacation_exists('sunny beach retreat', "Usa")

    # vacation_id = 3
    # vacation_name = "update name"
    # vacation_city = "update city"
    # Vacation_Description = "update description"
    # Start_Date = "2000-08-03"
    # End_date = '2000-11-03'
    # Price = 3200
    # Vacation_img = "update img.url"
    # country_name = "Holland"
    #
    # # func_works!!!
    # # vacation_logic.update_vacation(vacation_id, vacation_name,vacation_city,Vacation_Description,Start_Date,End_date,
    # #                                Price, Vacation_img,country_name)
    #
    # vacation_logic.del_vacation(4)


