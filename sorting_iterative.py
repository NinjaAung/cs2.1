def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) Best case while running inside a single loop 

    Memory usage: O(n) best case while holding the values of a list
    """
    if len(items) <= 1:
        return True
    for i in range(1,len(items)):
        if items[i] < items[i-1]:
            return False
    return True
        


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) Best Case under the assumption that items are no sorted and they are of nomral values and O(1) swaped

    Memory usage: O(n^2) Best Case under the assumption that stored variables are set of only a list of items 
    
    """
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
    Running time: O(n^2) Best Case under the assumption that items are comapred and O(1) when swaped

    Memory usage: O(n^2) Best Case when values are help in a double loop
    """
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
    Running time: O(n^2) Best Case when items are being sorted and swaped at O(1)
    Memory usage: O(n^2) Best Case when holding normal list
    """
    if is_sorted(items):
        return items
    for i in range(1,len(items)):
        head = i
        if items[i-1] > items[i]:
            while head > 0 and items[head-1] > items[head]:
                temp          = items[head-1]
                items[head-1] = items[head]
                items[head]   = temp
                head         -= 1

    return items
