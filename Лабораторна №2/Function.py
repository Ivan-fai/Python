def sum_of_even_num(x, y):
    sum_even = 0
    for i in range(x, y + 1):
        if x % 2 == 0:
            sum_even += i
    return sum_even