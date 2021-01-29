def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
    TODO: Memory usage: O(n) Why and under what conditions?
    """
    if not len(items):
        return True
    for i in range(1,len(items)):
        if items[i] < items[i-1]:
            return False
    return True
        


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: O(n) Why and under what conditions?"""
    while not is_sorted(items):
        for i in range(1,len(items)):
            if items[i] < items[i-1]:
                temp        = items[i]
                items[i]    = items[i-1]
                items[i-1]  = temp
    return items
            


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if is_sorted(items):
        return items
    for i in range(0,len(items)):
        min = float('inf')
        for j in range(i,len(items)):
            if min > items[j]:
                min = items[j]
                items[j] = items[i]
                items[i] = min
    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if is_sorted(items):
        return items
    for i in range(1,len(items)):
        sorted_index = i
        if items[i-1] > items[i]:
            while sorted_index > 0 and items[sorted_index-1] > items[sorted_index]:
                temp                  = items[sorted_index -1]
                items[sorted_index-1] = items[sorted_index]
                items[sorted_index]   = temp
                sorted_index  -= 1

    return items
