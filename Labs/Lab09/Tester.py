import Handler
import Sort

def test_cases():
    test_cases = Handler.load_test_lists()
    for idx, test_case in enumerate(test_cases, start=1):
        input_array = test_case["input"]
        expected_output = test_case["expected_output"]

        # Ensure custom_sort function is correct
        result = Sort.custom_sort(input_array)
        try:
            assert result == expected_output, f"Test Case {idx} Failed: {result} != {expected_output}"
        except AssertionError:
            print(f"Test Case {idx} Failed: {result} != {expected_output}") 
        print(f"Test Case {idx} Passed!")