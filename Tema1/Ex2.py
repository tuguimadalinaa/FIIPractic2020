from RedisManager import RedisEntity
import time


def cacher(*args, **kwargs):
    def Inner(func):
        def wrapper(*args_func, **kwargs_func):
            expiration_time = 100
            if len(args) == 0:
                if 'expiration_time' in kwargs.keys():
                    expiration_time = kwargs['expiration_time']
            else:
                expiration_time = args[0]
            func_result = func(*args_func, **kwargs_func)
            redis_entity.setKey(func.__name__, func_result, expiration_time)
            return func_result

        return wrapper

    return Inner


@cacher(expiration_time=180)
def functia_1(a, b):
    return a + b


@cacher(expiration_time=120)
def functia_2(a, b):
    return a * b


if __name__ == "__main__":
    global redis_entity
    redis_entity = RedisEntity("localhost", 6379)
    result = functia_1(10, 10)
    print(result)
    result = functia_2(10, 10)
    print(redis_entity.getKey('functia_1'))
    time.sleep(180)
    print(redis_entity.getKey('functia_1'))
    print(result)
