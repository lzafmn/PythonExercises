def diff_f(f, k, h ,x):
    '''f: the function; k: the order;
        h: the gap; x: the point'''
    if k <= 0:
        return f(x)
    else:
        return diff_f(f, k-1, h, x+h) - diff_f(f, k-1, h, x)
def diff_b(f, k, h ,x):
    '''f: the function; k: the order;
        h: the gap; x: the point'''
    if k <= 0:
        return f(x)
    else:
        return diff_f(f, k-1, h, x) - diff_f(f, k-1, h, x-h)
def diff_quo(f, I):
    if I == []:
        raise ValueError('Empty list!')
    elif len(I) == 1:
        return f(I[0])
    else:
        return (diff_quo(f, I[0:-1]) - diff_quo(f, I[1:]))/(I[0] - I[-1])
