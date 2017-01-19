def find_missing(list1, list2):
 
    if len(list1) and len(list2) == 0:
        return 0
    elif list1 == list2:
        return 0
    else:
        result = []
        for i in list2:
            if i not in list1:
                result.append(i)
        return result