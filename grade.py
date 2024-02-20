def grade(s):
    """
    >>> grade(4.99)
    'suspens'
    >>> grade(8)
    'notable'
    >>> grade(6.99)
    'aprovat'
    >>> grade(9.5)
    'excel.lent'
    >>> grade(10)
    'MH'
    """
    if s < 5:
        nota = "suspens"
    elif s >= 5 and s < 7:
        nota = "aprovat"
    elif s >= 7 and s < 9:
        nota = "notable"
    elif s >= 9 and s < 10:
        nota = "excel.lent"
    elif s == 10:
        nota = "MH"
    return nota


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
