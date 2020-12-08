# Write your code for lab 8C (remove) here.
from cal_ui import *


# create('anton')
# book("anton", 20, "sep", "12:00", "14:00", "Rob train")
# book("anton", 20, "sep", "15:00", "17:00", "Bomb train")
# show('anton', 20, 'sep')


def remove(cal_name: str, d: int, m: str, start_time: str):
    """Removes an appointment given by user"""
    day = new_day(d)
    month = new_month(m)
    cal_month = cy_get_month(month, get_calendar(cal_name))
    cal_day = cm_get_day(cal_month, day)
    time = new_time_from_string(start_time)

    new_cal_day = new_calendar_day(day, find_safe_appointments(cal_day, time))
    new_cal_month = cm_plus_cd(cal_month, new_cal_day)
    new_cal = cy_plus_cm(get_calendar(cal_name), new_cal_month)

    if get_calendar(cal_name) == new_cal:
        print('Could not remove appointment.')
    else:
        print('Appointment removed.')
        return insert_calendar(cal_name, new_cal)


def find_safe_appointments(cal_day: Day, time: Time) -> List:
    """Returns the non affected appointments"""
    safe_appointments = []
    for appointment in cd_iter_appointments(cal_day):
        if time != ts_start(app_span(appointment)):
            safe_appointments.append(appointment)
    return safe_appointments


# remove('anton', 20, 'sep', '12:00')

# show('anton', 20, 'sep')
