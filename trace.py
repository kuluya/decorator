import time


def trace(f):
    """ 計測デコレータ """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        return_val = f(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f.__name__, elapsed_time)

        return return_val

    return wrapper


@trace
def repetition(n):
    return recursion(n)


def recursion(n, pre=3):
    if n == 0:
        return pre

    return recursion(n - 1, 2 * pre + 3)


@trace
def recurrence(n):
    return 3 * 2 ** (n + 1) - 3


if __name__ == '__main__':
    repetition(500)
    recurrence(500)
