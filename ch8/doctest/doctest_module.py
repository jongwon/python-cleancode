
def convert_num(num_str: str):
    """
    >>> convert_num("12345")
    12345
    >>> convert_num("-12345")
    -12345
    >>> convert_num("12345-") # -를 뒤에 붙여도 -12345가 된다.
    -12345
    >>> convert_num("-12345-") # 특이 케이스 -(-12345) 가 되기 때문에 12345가 된다.
    12345
    """
    num, sign = num_str[:-1], num_str[-1]
    # print(num)
    if sign == "-":
        return -int(num)
    return int(num_str)
