#/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_b = len(tuple_b)
    len_a = len(tuple_a)

    if len_a == 0:
        a_item1 = 0
        a_item2 = 0
    elif len_a == 1:
        a_item1 = tuple_a[0]
        a_item2 == 0
    else:
        a_item1 = tuple_a[0]
        a_item2 = tuple_a[1]

    if len_b == 0:
        b_item1 = 0
        b_item2 = 0
    elif len_b == 1:
        b_item1 = tuple_b[0]
        b_item2 == 0
    else:
        b_item1 = tuple_b[0]
        b_item2 = tuple_b[1]

    new_tuple = (a_item1 + b_item1, a_item2 + b_item2)
    return new_tuple
