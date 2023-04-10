from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as date



if __name__ == '__main__':
    print('Текущая дата:', date.datetime.now().date())
    print(calculate_salary())
    print(get_employees())