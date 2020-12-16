#Christopher Wåtz chrwa634
#Anton Wegeström antwe841

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    #Test if the entire span is booked
    store_test_case(
        test_cases,
        2,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-21:00"],  # This day's appointments
        exp_result=[],
    )
    
    #Test for no appointments
    store_test_case(
        test_cases,
        3,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["08:00-21:00"],
    )

    #Test with minutes
    store_test_case(
        test_cases,
        4,
        start_str="08:15",  # Search interval starts
        end_str="21:30",  # Search interval ends
        booking_data=["07:52-09:32", "13:33-18:27"],  # This day's appointments
        exp_result=["09:32-13:33", "18:27-21:30"],
    )

    #Test with appointments directly after each other
    store_test_case(
        test_cases,
        5,
        start_str="08:15",  # Search interval starts
        end_str="21:30",  # Search interval ends
        booking_data=["07:53-09:32", "09:32-09:50", "13:33-18:27"],  # This day's appointments
        exp_result=["09:50-13:33", "18:27-21:30"],
    )

    # test if timespans after intervall
    store_test_case(
        test_cases,
        6,
        start_str="07:15",  # Search interval starts
        end_str="09:30",  # Search interva    l ends
        booking_data=["09:32-09:50", "13:33-18:27"],  # This day's appointments
        exp_result=["07:15-09:30"],
    )

    # #test if timespans before intervall
    store_test_case(
        test_cases,
        7,
        start_str="19:15",  # Search interval starts
        end_str="20:30",  # Search interval ends
        booking_data=["09:32-09:50", "13:33-18:27"],  # This day's appointments
        exp_result=["19:15-20:30"],
    )
    print("Test cases generated.")



    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
