#Christopher Wåtz chrwa634
#Anton Wegeström antwe841

from cal_abstraction import *
from cal_output import *

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
    """
    Creates a new time span sequence. If no timespan are given then
    return a timespan sequence with an empty sequence
    """

    if time_span is None:
        time_span = []

    else:
        ensure_list_type(time_span, TimeSpan)


    return TimeSpanSeq(time_span)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """return true if timespanseq is empty"""
    ensure_type(tss, TimeSpanSeq)

    return not tss.TimeSpan


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given TimeSpanSeq, where the given TimeSpan
    has been added in its proper position.
    """

    ensure_type(ts, TimeSpan)
    ensure_type(tss, TimeSpanSeq)
    def add_ts(ts: TimeSpan, tss: TimeSpanSeq):
        """add more or one timespans into a timespansequence"""
        if tss_is_empty(tss) or time_precedes(
            ts_start(ts), ts_start(tss.TimeSpan[0])
        ):
            return [ts] + tss.TimeSpan
        else:
            return [tss.TimeSpan[0]] + add_ts(ts, new_time_span_seq(tss.TimeSpan[1:]))

    return new_time_span_seq(add_ts(ts, tss))


def tss_iter_spans(tss: TimeSpanSeq):
    """iterates over a timespan sequence"""
    ensure_type(tss, TimeSpanSeq)

    for ts in tss.TimeSpan:
        yield ts


def show_time_spans(tss: TimeSpanSeq) -> None:
    """shows all the timespans in a timespan sequence"""
    ensure_type(tss, TimeSpanSeq)

    for ts in tss_iter_spans(tss):
        show_ts(ts)
        print()

# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(span, result)

    return result
