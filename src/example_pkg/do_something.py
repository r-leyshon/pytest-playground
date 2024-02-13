"""Simple modules to exemplify unit & end to end tests."""


def double_a_number(some_num:int) -> int:
    return 2 * some_num


def half_a_number(some_num:int) -> float:
    return float(0.5 * some_num)


def wrap_n_write_txt(num:int, pth:str) -> None:
    n = double_a_number(num)
    n = double_a_number(n)
    n = half_a_number(n)
    with open(pth, "w") as f:
        f.writelines(str(n))
        f.close()
    return None
