import RedisManager
import functools


def cacher(*args, **kwargs):
    def Inner(func):
        def wrapper(*args_func, **kwargs_func):
            expiration_time = 100
            if len(args) == 0:
                if 'expiration_time' in kwargs.keys():
                    expiration_time = kwargs['expiration_time']
            else:
                expiration_time = args[0]
            result = func(*args_func, **kwargs_func)
            conenction.set(func.__name__, result, ex=expiration_time)
            return result

        return wrapper

    return Inner


@cacher(expiration_time=180)
def functia_1(a, b):
    return a + b


@cacher(expiration_time=120)
def functia_2(a, b):
    return a * b


if __name__ == "__main__":
    connection = RedisManager.redis_connect("localhost", 6379)
    global conenction
    result = functia_1(10, 10)
    print(result)
    result = functia_2(10, 10)
    print(result)
