'''
    Write a program to check employee entry time using the following algorithm:
    If some employee entry more than one time within hour
        then we need to return particular employee name.

    input1 = ["cris", "peter", "gorge", "Hendry", "jatin", "cris", "Hendry", "Malik", "peter"]
    input2 = ["11:30", "12:10", "14:00", "16:00", "10:40", "12:00", "15:40", "15:30", "16:00"]

    Output: ["cris","Hendry"]
'''

from collections import defaultdict
from datetime import datetime

def check_employee_entry_time(emp_names, entry_time):
    '''
        Function to check employee entry time
    '''
    emp_data = defaultdict(list)
    for i, emp_name in enumerate(emp_names):
        emp_data[emp_name].append(entry_time[i])

    output = []
    for emp_name, time_data in emp_data.items():
        time_data.sort()
        if len(time_data) > 1 and (datetime.strptime(time_data[1], '%H:%M') -
                    datetime.strptime(time_data[0], '%H:%M')).seconds < 3600:
            output.append(emp_name)
    return output


if __name__ == '__main__':
    input1 = ["cris", "peter", "gorge", "Hendry", "jatin", "cris", "Hendry", "Malik", "peter"]
    input2 = ["11:30", "12:10", "14:00", "16:00", "10:40", "12:00", "15:40", "15:30", "16:00"]
    print(check_employee_entry_time(input1, input2))
