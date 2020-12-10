
from cal_ui import *


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


def tests():
    """Tests the functions"""
    def test1():
        """First test"""
        create("Jayne")
        book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
        book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
        show("Jayne", 20, "sep")
        remove("Jayne", 20, "sep", "15:00")
        book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")

        correct_cal = CalendarYear(months=[CalendarMonth
        (month=Month(name='september'), days=[CalendarDay(day=Day(number=20),
        appointments=[Appointment(span=TimeSpan(start=Time(hour=Hour(number=12),
        minute=Minute(number=0)), end=Time(hour=Hour(number=14),
        minute=Minute(number=0))), subject=Subject(text='Rob train')),
        Appointment(span=TimeSpan(start=Time(hour=Hour(number=15),
        minute=Minute(number=0)), end=Time(hour=Hour(number=16),
        minute=Minute(number=0))), subject=Subject(text='Return loot'))])])])

        assert get_calendar('Jayne') == correct_cal

    def test2():
        """First test"""
        create("Carl")
        book("Carl", 10, "sep", "12:00", "14:00", "Eat cookie")
        book("Carl", 10, "sep", "15:00", "16:00", "Bake a cake")
        show("Carl", 10, "sep")
        remove("Carl", 10, "sep", "19:00")
        book("Carl", 10, "sep", "19:00", "20:00", 'Build a sand castle')
        book('Carl', 10, 'sep', '21:53', '21:54', 'Eat icecream')
        remove('Carl', 10, 'sep', '19:00')


        correct_cal2 = CalendarYear(months=[CalendarMonth(month=Month
        (name='september'), days=[CalendarDay(day=Day(number=10),
        appointments=[Appointment(span=TimeSpan(start=Time(hour=Hour(number=12),
        minute=Minute(number=0)), end=Time(hour=Hour(number=14),
        minute=Minute(number=0))), subject=Subject(text='Eat cookie')),
        Appointment(span=TimeSpan(start=Time(hour=Hour(number=15),
        minute=Minute(number=0)), end=Time(hour=Hour(number=16),
        minute=Minute(number=0))), subject=Subject(text='Bake a cake')),
        Appointment(span=TimeSpan(start=Time(hour=Hour(number=21),
        minute=Minute(number=53)), end=Time(hour=Hour(number=21),
        minute=Minute(number=54))), subject=Subject(text='Eat icecream'))])])])

        assert get_calendar('Carl') == correct_cal2


    test1()
    test2()
    print('Passed all tests')
tests()
