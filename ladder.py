def my_steps(n: int) -> int:
    if n not in range(1, 26):
        raise ValueError;

    if n <= 2: 
        return n;
    return my_steps(n - 1) + my_steps(n - 2);

