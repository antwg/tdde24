# Write your code for lab 8d here.
from cal_abstraction import *
from cal_ui import *
from settings import CHECK_AGAINST_FACIT
from cal_ui import *
from lab8b import *

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *

def last_ts_in_seq(time_span_seq:TimeSpanSeq) -> TimeSpan:
    """Returns the last TimeSpan in a TimeSpanSeq"""
    print(time_span_seq)
    return time_span_seq.TimeSpan[-1]


def show_free(cal_name: str, d: int, m: str, start_time: str, end_time: str):
    """Prints free timespans given a day and a start and end time."""
    start = new_time_from_string(start_time)
    end = new_time_from_string(end_time)
    month = new_month(m)
    day = new_day(d)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(new_month(m), cal_year)
    cal_day = cm_get_day(cal_month, new_day(d))

    show_time_spans(free_spans(cal_day, start, end))


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """Finds free timespans given a CalendarDay and a start and end time."""
    time_span_seq = new_time_span_seq()

    if cd_is_empty(cal_day):  # If day empty, return TimeSpan from start to end
        return new_time_span_seq([new_time_span(start, end)])

    else:  # Add all appointments to a TimeSpanSeq
        for app in cd_iter_appointments(cal_day):
            time_span_seq = tss_plus_span(time_span_seq, app_span(app))

        free_time = new_time_span_seq()
        old_time_start = start
        for ts in tss_iter_spans(time_span_seq):
            ts_s = ts_start(ts)
            ts_e = ts_end(ts)

            if time_precedes(ts_e, start):  # TimeSpan before given start
                pass
            
            else:
                if not time_precedes_or_equals(ts_s, old_time_start):
                    if time_precedes_or_equals(ts_s, end):
                        free_time = tss_plus_span(free_time, new_time_span(old_time_start, time_earliest(ts_s, end)))
                        old_time_start = time_earliest(ts_e, end)
                    elif end == old_time_start:
                        pass
                else:
                    old_time_start = ts_e

        if time_precedes(ts_end(last_ts_in_seq(time_span_seq)), end):
            free_time = tss_plus_span(free_time, new_time_span(ts_end(last_ts_in_seq(time_span_seq)), end))


        return free_time

# create("Jayne")
# book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
# book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
# show_free("Jayne", 20, "sep", "08:00", "19:00")
