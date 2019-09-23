def list_to_string(l):
    """
    Converts the given list of strings into a single string by appending them all together. Calls the str() built-in
    function on every element inside l, so a string is always created.
    :param l: the list of values to convert to a string
    :return: l converted to a single string
    :raises: TypeError - if vals is not iterable
    """
    ret = ""
    for v in l:
        ret += str(v)
    return ret


def is_list(l):
    """
    :param l: the object to check if it is a list
    :return: True if l is a list of some kind, False otherwise. Dictionaries are not lists
    """
    try:
        for _ in l:
            pass
        return not isinstance(l, dict)
    except TypeError:
        return False


def linearize_list(l):
    """
    Converts l to be a list containing no sub-lists.
    If l is not a list, l is converted into a list of size 1.
    All empty lists are ignored.
    Dictionaries are not considered lists.
    :param l: the list to linearize
    :return: the linearized list
    """
    if not is_list(l):
        return [l, ]

    ret = []
    for element in l:
        if is_list(element):
            ret += linearize_list(element)
        else:
            ret.append(element)

    return ret
