import doctest


def add_one(num:int) -> int:
    """
    >>> add_one(1)
    2
    >>> add_one(-1)
    -1
    """
    return num+1


def abs(num:int) -> int:
    """
    >>> abs(10)
    10
    >>> abs(-10)
    10
    >>> abs(0)
    0
    """
    if(num<0) :
        return -1*num
    return num

if __name__ == '__main__':
    doctest.testmod()