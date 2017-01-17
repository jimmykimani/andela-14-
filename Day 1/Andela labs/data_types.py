def data_type(n):
    if isinstance(n, str):  # check if string
        return len(n)
    elif isinstance(n, bool):  # check if boolean
        return n
    elif isinstance(n, int):  # check if integer
        if n < 100:
            return 'less than 100'
        elif n > 100:
            return 'more than 100'
        elif n == 100:
            return 'equal to 100'
    elif isinstance(n, list):  # check if list
        if len(n) >= 3:
            return n[2]
        else:
            return None
    else:  # cater for other data types passed
        return 'no value
