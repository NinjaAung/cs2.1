#!python
def what_sort(numbers):
    min = max = numbers[0]
    for i in range(0,len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
        if numbers[i] > max:
            max = numbers[i]
    lst = [None] * max
    lst[0] = min
    lst[len(lst)-1] = max
    for i in range(0,len(numbers)):
        if not numbers[i] == min and not numbers[i] == max:
            lst[numbers[i]-1] = numbers[i]
    j = 0
    for i in range(0,len(lst)):
        if lst[i] is not None:
            numbers[j] = lst[i]
            j += 1

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n+k) Average Case when there is a small semi small range
    TODO: Memory usage: O(n+k) Average Case when there is a small semi small range"""
    min = max = numbers[0]

    # find min / max values
    for i in range(0,len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
        if numbers[i] > max:
            max = numbers[i]

    # Counting
    k  = 0
    lst = [0] * (max+1)
    for i in range(min,max+1):
        for j in range(0,len(numbers)):
            if i == numbers[j]:
                lst[k] = lst[k] + 1
        k += 1
        
    # Shift values
    for i in range(1,len(lst)):
        lst[i] = lst[i]+lst[i-1]

    #  Mutate given list
    j = k = 0
    lst = [0] + lst[:len(lst)-1]
    value = min

    while j < len(numbers):
        if k >= len(lst)-1:
            numbers[j] = value
            j += 1
            continue

        if lst[k] <= j and j < lst[k+1]:
            numbers[j] = value
            j += 1
            continue
        k += 1
        value += 1

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
