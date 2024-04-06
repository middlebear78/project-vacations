
class VacationModel:
    def __init__(self, vacation_id, vacation_name, vacation_city, vacation_description, start_date, end_date, price,
                 vacation_img, country_id):

        self.vacation_id = vacation_id
        self.vacation_name = vacation_name
        self.vacation_city = vacation_city
        self.vacation_description = vacation_description
        self.start_Date = start_date
        self.end_date = end_date
        self.price = price
        self.vacation_img = vacation_img
        self.country_id = country_id

    def __str__(self):
        return (f"Vacation ID: {self.vacation_id}\n"
                f"Vacation Name: {self.vacation_name}\n"
                f"Vacation City: {self.vacation_city}\n"
                f"Description: {self.vacation_description}\n"
                f"Start Date: {self.start_Date}\n"
                f"End date: {self.end_date}\n"
                f"Price: {self.price}\n"
                f"Photo: {self.vacation_img}\n"
                f"Country ID: {self.country_id}"
                )


    @staticmethod
    def dict_to_vacation(dict):
        vacation_id, vacation_name, vacation_city = dict["Vacation_id"], dict["vacation_name"],dict["vacation_city"]
        vacation_description, start_date, end_date = dict["Vacation_Description"], dict["Start_Date"],dict["End_date"]
        price, vacation_img, country_id = dict["Price"], dict["Vacation_img"],dict["Country_id"]
        vacation = VacationModel(
            vacation_id, vacation_name, vacation_city,
            vacation_description, start_date, end_date,
            price, vacation_img, country_id
        )
        return vacation

    @staticmethod
    def dicts_to_vacations(dicts_list):
        return [VacationModel.dict_to_vacation(item) for item in dicts_list]


if __name__ == '__main__':
    vacation1 = {
        "Vacation_id": 1,
        "vacation_name": "Summer Retreat",
        "vacation_city": "Beach Town",
        "Vacation_Description": "Relaxing beach vacation",
        "Start_Date": "2024-07-01",
        "End_date": "2024-07-10",
        "Price": 1000,
        "Vacation_img": "summer.jpg",
        "Country_id": 1
    }
    vacation = VacationModel.dict_to_vacation(vacation1)
    print(vacation)

    vacation2 = {
        "Vacation_id": 2,
        "vacation_name": "Mountain Escape",
        "vacation_city": "Mountain Village",
        "Vacation_Description": "snowy mountain retreat",
        "Start_Date": "2024-08-15",
        "End_date": "2024-08-25",
        "Price": 12000,
        "Vacation_img": "whatever.jpg",
        "Country_id": 2
    }

    dicts_lists = [vacation1, vacation2]

    vacations = VacationModel.dicts_to_vacations(dicts_lists)
    for vacation in vacations:
        print()
        print(vacation)
        print()