# Write your code for lab 8d here.

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

    store_test_case(
    """Test if the entire span is booked"""
        test_cases,
        2,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-21:00"],  # This day's appointments
        exp_result=[],
    )

    store_test_case(
    """Test for no appointments"""
        test_cases,
        3,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["08:00-21:00"],
    )

    store_test_case(
    """Test with minutes"""
        test_cases,
        4,
        start_str="08:15",  # Search interval starts
        end_str="21:30",  # Search interval ends
        booking_data=["07:52-09:32", "13:33-18:27"],  # This day's appointments
        exp_result=["09:32-13:33", "18:27-21:30"],
    )

    store_test_case(
    """Test with appointments directly after each other"""
        test_cases,
        5,
        start_str="08:15",  # Search interval starts
        end_str="21:30",  # Search interval ends
        booking_data=["07:52-09:32", "09:32-09:50", "13:33-18:27"],  # This day's appointments
        exp_result=["09:50-13:33", "18:27-21:30"],
    )
    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
