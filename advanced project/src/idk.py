def add_vacation(self):
    self.vacation_logic.add_vacation(
        input("Enter vacation name: "),
        input("Enter vacation city name: "),
        input("Enter vacation description: "),
        input("Enter start date: "),
        input("Enter end date: "),
        input("Enter price: "),
        input("Enter vacation image URL: "),
        input("Enter country name: ")
    )