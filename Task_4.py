class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(self, new_hourly_payment):
        EmployeeSalary.hourly_payment = new_hourly_payment

    def salary(self):
        current_hours = self.get_hours()
        return current_hours * EmployeeSalary.hourly_payment