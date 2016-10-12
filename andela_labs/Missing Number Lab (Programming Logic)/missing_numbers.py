

def find_missing(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)

    list_a = sorted(list_a)
    list_b = sorted(list_b)

    if len_a == len_b:
        return 0

    common_len = -1
    if (len_a > len_b):
        common_len = len_b
    else:
        common_len = len_a

    start = 0
    end = common_len - 1

    while start <= end:
        mid_point = common_len // 2

        if list_a[mid_point] == list_b:
            start = mid_point + 1
        else:
            return list_a[mid_point]