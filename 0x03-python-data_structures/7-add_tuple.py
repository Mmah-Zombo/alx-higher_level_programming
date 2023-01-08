#/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = ()
    if len(tuple_a) < 2:
        tuple_a[1] = 0;
