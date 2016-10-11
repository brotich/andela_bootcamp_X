

def find_max_min(list_numbers):
    """
       takes a list_numbers and returns min and max values
       as list i.e  [min, max]
    """

    if not isinstance(list_numbers, list):
        raise TypeError("expected list_numbers to be a list")

    list_length = len(list_numbers)

    # remove duplicates values and sort values ascending
    list_numbers = sorted(set(list_numbers))

    length = len(list_numbers)

    if (length > 1):
        return [list_numbers[0], list_numbers[length - 1]]

    return [list_length]  # one unique value
