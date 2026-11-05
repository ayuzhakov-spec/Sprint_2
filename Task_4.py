class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        # Сохраняем переданные значения в атрибуты конкретного сотрудника
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        # Если часы не указаны (None), рассчитываем их по формуле
        if self.hours is None:
            # Формула из задания
            self.hours = (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        # Если email не указан, генерируем его
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email

    def set_hourly_payment(self, new_hourly_payment):
        # Меняем значение переменной класса (общее для всех)
        EmployeeSalary.hourly_payment = new_hourly_payment

    def salary(self):
        # Чтобы получить часы, вызываем метод get_hours(), 
        # так как там есть логика расчета, если hours = None
        current_hours = self.get_hours()
        return current_hours * EmployeeSalary.hourly_payment