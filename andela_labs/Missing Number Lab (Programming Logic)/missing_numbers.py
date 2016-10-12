

def find_missing(list_a, list_b):

    """
        it takes  list_a and list_b, which defers by one item,
        and returns the extra number in the longer list
        :parameter list_a list containing the int items
        :parameter list_b list containing the int items
        return: the extra number in the longer list
    """

    if not isinstance(list_a, list):
        raise TypeError("Expected list_a to be a list")

    if not isinstance(list_b, list):
        raise TypeError("Expected list_b to be a list")

    NUM_START_LIST = -1

    len_a, len_b = len(list_a), len(list_b)  # get length of array

    if len_a == len_b:                       # the list are equal
        return 0

    list_a, list_b = sorted(list_a), sorted(list_b)

    list_a_is_longer = len_a > len_b

    common_len = len_b if list_a_is_longer else len_a  # determine shorter list

    first = 0
    last = common_len - 1
    dif_index = -1

    found = False

    while first <= last and not found:          # binary search comparing the
        midpoint = (first + last) / 2           # list at index midpoint
        if list_a[midpoint] != list_b[midpoint]:
                found = True
                dif_index = midpoint
        else:
            if list_a[midpoint] < list_b[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if dif_index > NUM_START_LIST:       # if dif > NUM_START_LIST, missing number
        if list_a_is_longer:             # at startof array
            return list_a[0]
        return list_b[0]

    if list_a_is_longer:
        return list_a[common_len]
    return list_b[common_len]

