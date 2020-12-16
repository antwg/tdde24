#Christopher Wåtz chrwa634
#Anton Wegeström antwe841

from cal_abstraction import *
from cal_ui import *
from settings import CHECK_AGAINST_FACIT
from cal_ui import *

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

def show_free(cal_name: str, d: int, m: str, start_time: str, end_time: str) -> None:
    """Prints free timespans given a day and a start and end time."""
    start = new_time_from_string(start_time)
    end = new_time_from_string(end_time)
    month = new_month(m)
    day = new_day(d)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(new_month(m), cal_year)
    cal_day = cm_get_day(cal_month, new_day(d))
    if cd_is_empty(cal_day):
        print('There are no appointment this day')
    else:
        show_time_spans(free_spans(cal_day, start, end))


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """Finds free timespans given a CalendarDay and a start and end time."""
    time_span_seq = new_time_span_seq()

    #takes out all the timespan of all the appointments add it to a timespansequence
    for app in cd_iter_appointments(cal_day):
        time_span_seq = tss_plus_span(time_span_seq, app_span(app))

    free_time = new_time_span_seq()
    point = start
    for ts in tss_iter_spans(time_span_seq):
        ts_s = ts_start(ts)
        ts_e = ts_end(ts)

        if time_precedes_or_equals(ts_s, point):
            #Must be outside the given intervall
            if time_precedes(ts_e, point):
                pass
            #we must reach the end if timespan finish after our interval
            elif time_precedes_or_equals(end, ts_e):
                point = ts_e
                break
            #move point for next timespan
            elif time_precedes_or_equals(point, ts_e):
                point = ts_e
                pass
            else:
                pass #if we want to do something later
        
        #if the start of the time span is after the point
        elif time_precedes(point, ts_s):
            #than it must be out side the interval
            if time_precedes_or_equals(end, ts_s):
                free_time = tss_plus_span(free_time, new_time_span(point, end))
                point = ts_e
                break
            #then it must be the end of the interval but we need to add between
            #point and ts
            if time_precedes_or_equals(end, ts_e):
                free_time = tss_plus_span(free_time, new_time_span(point, ts_s))
                point = ts_e
                break
            #the time span is in the interval
            elif time_precedes(ts_e, end):
                free_time = tss_plus_span(free_time, new_time_span(point, ts_s))
                point = ts_e
                pass

        else:
            pass #if we want to have a raise syntaxerror
        
    #If point is still in the interval then we need to add the last part between point and end
    if time_precedes(point, end):
        free_time = tss_plus_span(free_time, new_time_span(point, end))

    return free_time
