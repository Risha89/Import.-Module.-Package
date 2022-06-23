import application.salary
import application.people
from datetime import datetime

a = application.salary.calculate_salary(2)
b = application.people.get_employees(2)
dt = datetime.now()

if __name__ == '__main__':
    print(a + b)
    print(datetime.date(dt))

