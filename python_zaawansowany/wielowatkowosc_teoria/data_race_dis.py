import dis


def inc(x):
    x += 1


dis.dis(inc)
