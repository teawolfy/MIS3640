def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None #what do you mean by this?

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    for i in range(len(t)):
        t =  t.pop(0) and t.pop(2)
        return t

t = [1, 2, 3, 4]

chop(t)
print(t)