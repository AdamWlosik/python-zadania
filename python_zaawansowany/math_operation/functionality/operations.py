def calc_power(base, exp):
    return base ** exp


def calc_arith_seq_sum(start, end):
    sum = 0

    for i in range(start, end + 1):
        sum += i

    return sum
