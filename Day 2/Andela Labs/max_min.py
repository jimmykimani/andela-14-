def find_max_min(a_list):

    sorted_list = sorted(a_list, key=int)
    min_max_list = [sorted_list[0], sorted_list[len(sorted_list) - 1]]


    if min_max_list[0] == min_max_list[len(min_max_list) - 1]:
        return [len(sorted_list)]
    else:
        return min_max_list

print(find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]))
