from cal_abstraction import *

# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple(
    "TimeSpanSeq", [("TimeSpan", TimeSpan)]
)

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(time_span: TimeSpan = None) -> TimeSpanSeq:
    
    if time_span is None:
        time_span = []
    
    # elif isinstance(time_span, list):
    #     for ts in time_span:
    #         ensure_type(ts, TimeSpan)

    else:
        ensure_list_type(time_span, TimeSpan)
 
    
    return TimeSpanSeq(time_span)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """return true if there is no timespan in the timespan seq"""
    ensure_type(tss, TimeSpanSeq)

    return not tss.TimeSSpan


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given TimeSpanSeq, where the given TimeSpan
    has been added in its proper position.
    """

    ensure_type(ts, TimeSpan)   
    ensure_type(tss, TimeSpanSeq)

    def take_out_the_timespan(tss):

        if not tss.TimeSpan:
            return []
        
        elif isinstance(tss.TimeSpan, list):
            
            return tss.TimeSpan
        
        else:
            return [tss.TimeSpan]

    def add_time_span(timespan: TimeSpan):

        if not timespan:
            return []

        else:
            return [timespan]

    time_span_added = add_time_span(ts) + take_out_the_timespan(tss)
    time_span_added.sort(key=ts_start)

    return new_time_span_seq(time_span_added)


def tss_iter_spans(tss: TimeSpanSeq):
    ensure_type(tss, TimeSpanSeq)

    for ts in tss.TimeSpan:
        yield ts


def show_time_spans(tss: TimeSpanSeq) -> None:
    ensure_type(tss, TimeSpanSeq)
    
    def show_timespan(tss):
        print('Timespan sequence:')
        for ts in tss.TimeSpan:

            timespan = [hour_number(ts_start(ts).hour), minute_number(ts_start(ts).minute),
            hour_number(ts_end(ts).hour), minute_number(ts_end(ts).minute)]

            time= []
            for elem in timespan:
                if elem < 10:
                    time.append('0' + str(elem))
                else:
                    time.append(str(elem))
            
            print(time[0], ':', time[1], ' - ', time[2], ':', time[3], sep='')

    show_timespan(tss)

    # print(hour_number(ts_start(ts).hour),':', minute_number(ts_start(ts).minute),' - ',
    # hour_number(ts_end(ts).hour), ':', minute_number(ts_end(ts).minute), sep='')


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(span, result)

    return result

span1 = new_time_span(new_time(new_hour(3), new_minute(45)), new_time(new_hour(4), new_minute(0)))
span2 = new_time_span(new_time(new_hour(5), new_minute(45)), new_time(new_hour(6), new_minute(0)))
span3 = new_time_span(new_time(new_hour(2), new_minute(45)), new_time(new_hour(2), new_minute(55)))

a = new_time_span_seq()
b = new_time_span_seq([span2])

# print(a)
# print(b)

# print(tss_is_empty(a))
# print(tss_is_empty(b))

print('done with first:')
a = tss_plus_span(a, span1)
print(a)

print('done with second:')
a = tss_plus_span(a, span2)
print(a)
print('done with third:')
a = tss_plus_span(a, span3)
print(a)

show_time_spans(a)

# print(tss_plus_span(b, span2))
# print(tss_plus_span(c, span3))

# print(tss_is_empty(b))
# print(tss_is_empty(c))
# print(tss_plus_span(a, span1))
# print(tss_plus_span(b, span2))
# print(tss_plus_span(c, span3))