sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2,7,7,9,0,0,11,-5,-3]

def remove_set(sample_list):
    result_list = list(set(sample_list))
    result_list.sort()
    return result_list


def remove_for(input_list):
    result_list = []
    for item in sample_list:
        if item not in result_list:
            result_list.append(item)
    result_list.sort()
    return result_list

def remove_coll(input_list):
    dict = {}
    for item in input_list:
        dict[item] = None
    result_list = list(dict.keys())
    result_list.sort()
    return result_list

print(remove_for(sample_list))
print(remove_set(sample_list))
print(remove_coll(sample_list))
#print_list(remove_enum(sample_list))

