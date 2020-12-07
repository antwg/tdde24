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

def new_time_span_seq(time_span -> TimeSpan) -> TimeSpanSeq:
    ensure_type(time_span, TimeSpan)
    if time_span is None:
        time_span = None
    else:
        ensure_list_type(time_span)
    
    return TimeSpanSeq(time_span)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """return true iff the given CalendarDay has no appointments."""
    ensure_type(tss, TimeSpanSeq)
    return not tss.TimeSpan


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


def tss_iter_spans(tss):
    pass


def show_time_spans(tss):
    pass


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(span, result)

    return result
