# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      Sorts an array of numbers using the segregation sort method.
# 4. What was the hardest part? Be as specific as possible.
#      It when great, until I ran it and found a bug that was messing with the printing of the array, and that it was
#      not sorting the array correctly. I had to go back and redesign the sorting algorithm.
# 5. How long did it take for you to complete the assignment?
#      2 hours
# 6. YouTube Link:
#      https://www.youtube.com/watch?v=V1gSCVMkrpY&ab_channel=school
import Handler


def segregation_sort(array, i_start=0, i_end=None):
    if i_end is None:
        i_end = len(array) - 1
    if i_start < i_end:
        i_pivot = partition(array, i_start, i_end)

        segregation_sort(array, i_start, i_pivot - 1)
        segregation_sort(array, i_pivot + 1, i_end)

    return array

def partition(array, i_start, i_end):
    pivot_index = (i_start + i_end) // 2
    pivot_value = array[pivot_index]

    # Move pivot to the end
    array[pivot_index], array[i_end] = array[i_end], array[pivot_index]

    i_up = i_start
    for i in range(i_start, i_end):
        if array[i] < pivot_value:
            array[i_up], array[i] = array[i], array[i_up]
            i_up += 1

    # Move pivot to its final position
    array[i_up], array[i_end] = array[i_end], array[i_up]

    return i_up

test_cases = Handler.load_test_lists()
for idx, test_case in enumerate(test_cases, start=1):
    input_array = test_case["input"]
    array1 = input_array.copy()
    expected_output = test_case["expected_output"]

    result = segregation_sort(array1)
    print(f"input: {input_array}")
    print(f"result: {result}")
    print(f"expected: {expected_output}")
    print()