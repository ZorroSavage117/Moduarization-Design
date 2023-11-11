def combine(source, destination, begin1, begin2, end2):
    end1 = begin2

    for i in range(begin1, end2):
        if (begin1 < end1) and (begin2 == end2 or source[begin1] < source[begin2]):
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1
    return destination

def custom_sort(array):
    size = len(array)
    source = array
    destination = [0] * size
    number = 2

    while number > 1:
        number = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and source[end1 - 1] <= source[end1]:
                end1 += 1

            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and source[end2 - 1] <= source[end2]:
                end2 += 1

            number += 1
            combine(source, destination, begin1, begin2, end2)
            begin1 = end2

        source, destination = destination, source

    return source

