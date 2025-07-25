class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email


    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours == -1:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email == '':
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, n_hourly_payment):
        cls.hourly_payment = n_hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
# напиши свой код здесь