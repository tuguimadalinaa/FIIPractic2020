import redis


def redis_connect(host_name, port_number) -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=host_name,
            port=port_number,
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")

