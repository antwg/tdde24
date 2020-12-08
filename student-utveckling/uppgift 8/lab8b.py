from cal_abstraction import *

# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple(
    "TimeSpanSeq", [("timespan", TimeSpan)]
)

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(time_span: TimeSpan = None) -> TimeSpanSeq:
    
    if time_span is None:
        time_span = []
    
    else:
        ensure_type(time_span, TimeSpan)
 
    
    return TimeSpanSeq(time_span)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """return true if there is no timespan in the timespan seq"""
    ensure_type(tss, TimeSpanSeq)

    if len(tss[0]) > 0:
        return False
    
    else:
        return True


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given TimeSpanSeq, where the given TimeSpan
    has been added in its proper position.
    """
    ensure_type(ts, TimeSpan)
    ensure_type(tss, TimeSpanSeq)

    def add_time_span(timespan: TimeSpan):
        if not timespan:
            return []
        else:
            return [timespan[0] + add_time_span(timespan[1:])]
    
    return tss + new_time_span_seq(add_time_span(ts))


# def tss_iter_spans(tss):
#     pass


# def show_time_spans(tss):
#     pass


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(span, result)

    return result


a = new_time_span_seq()
print(a)
b = new_time_span_seq(new_time_span(new_time(new_hour(1), new_minute(45)), new_time(new_hour(3), new_minute(0))))
print(b)
print(tss_is_empty(a))
print(tss_is_empty(b))
span = new_time_span(new_time(new_hour(5), new_minute(45)), new_time(new_hour(6), new_minute(0)))
print(tss_plus_span(a, span))
