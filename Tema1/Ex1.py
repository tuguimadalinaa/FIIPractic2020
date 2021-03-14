import functools


def calls_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    wrapper.calls = 0
    return wrapper


@calls_counter
def functia1():
    pass


@calls_counter
def functia2():
    pass


if __name__ == "__main__":
    functia1()
    functia2()
    functia1()
    functia2()
    functia2()
