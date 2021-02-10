#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    merged_list = []

    items1_is_full = len(items1)
    items2_is_full = len(items2)

    while items1_is_full and items2_is_full:

        if items1[0] < items2[0]:
            merged_list.append(items1.pop(0))
        else:
            merged_list.append(items2.pop(0))

        items1_is_full = len(items1)
        items2_is_full = len(items2)

    if not items1_is_full:
        merged_list += items2
        return merged_list

    if not items2_is_full:
        merged_list += items1
        return merged_list


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items) & 1:
        print("Len of items is not even")
        return

    if len(items) > 1:
        mid = len(items)//2

        left_sub = items[:mid]
        right_sub = items[mid:]

        merge_sort(left_sub)
        merge_sort(right_sub)

        i = j = k = 0

        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] < right_sub[j]:
                items[k] = left_sub[i]
                i += 1
            else:
                items[k] = right_sub[j]
                j += 1
            k += 1

        while i < len(right_sub):
            items[k] = left_sub[i]
            i += 1
            k += 1

        while j < len(right_sub):
            items[k] = right_sub[j]
            j += 1
            k += 1


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    i = (low-1)
    pivot = items[high]

    for j in range(low, high):

        if items[j] <= pivot:

            i = i+1
            items[i], items[j] = items[j], items[i]

    items[i+1], items[high] = items[high], items[i+1]
    return (i+1)


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if low is None:
        return quick_sort(items,0,high)

    if high is None:
        return quick_sort(items,low,len(items)-1)
    if len(items) == 1:
        return items
    if low < high:
        partioned_i = partition(items, low, high)

        quick_sort(items, low, partioned_i-1)
        quick_sort(items, partioned_i+1, high)

