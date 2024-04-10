def do_some_work(x: int) -> int:
    """Efficiently computes a simple polynomial just for kicks

    5 + 3x + 4x^2
    """
    return 5 + x * (3 + x * (4))