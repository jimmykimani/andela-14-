def words(n):
    result = {}
    # if the digit value is not a string
    for i in n.split():
        if not i.isdigit():
            if result.get(i):
                result[i] += 1
            else:
                result[i] = 1

    for i in n:
        #  if the digit value is a string
        if i.isdigit():
            i = int(i)
            if result.get(i):
                result[i] += 1
            else:
                result[i] = 1

    return result
