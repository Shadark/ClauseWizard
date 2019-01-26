from collections import defaultdict

tree = lambda: defaultdict(tree)


def is_phrase(list_struct):
    return ((isinstance(list_struct, list)) and
            (len(list_struct) == 2) and (not isinstance(list_struct[0], list)) and
            (isinstance(list_struct[1], list)))


def convert_to_phrase(list_struct):
    return list_struct[0], list_struct[1]


def insert_check_dup(key, val, dic):
    if key in dic:  # Duplicate
        if isinstance(dic[key], list):  # Already existing duplicates
            dic[key].append(format_item(val))
        else:  # First duplicate, concatenate with previous value
            dic[key] = [dic[key], format_item(val)]
    else:
        dic[key] = format_item(val)
    return dic


def format_item(list_struct):  # Always a list
    if (len(list_struct) == 1) and (not isinstance(list_struct[0], list)):  # Single data item
        return list_struct[0]
    else:
        if is_phrase(list_struct[0]):  # Only phrases inside this list
            dic = tree()
            for elem in list_struct:
                (key, val) = convert_to_phrase(elem)
                dic = insert_check_dup(key, val, dic)
            return dic
        else:  # Only data items/objects
            values = []
            for elem in list_struct:
                values.append(format_item(elem))
            return values


def format_full(result_list):
    dic = tree()
    for elem in result_list:
        (key, val) = convert_to_phrase(elem)
        dic = insert_check_dup(key, val, dic)

    return dic
