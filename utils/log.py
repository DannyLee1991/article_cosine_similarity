import time


def progress(index, size, for_what='当前进度', step=10):
    block_size = int(size / step)
    if index % block_size == 0:
        crt = int(index / block_size)
        print('%s ==> [%d / %d]' % (for_what, crt, step))


def log_time():
    def _log_time(func):
        # func()
        def wrapper(*args, **kwargs):
            print("start")
            start_time = time.time()
            result = func() if len(args) == len(kwargs) == 0 else func(*args, **kwargs)
            end_time = time.time()
            cost_time = end_time - start_time
            print("[%s] cost time -> %s" % (func.__name__, cost_time))
            return result

        return wrapper

    return _log_time


def line(log_str, style='-'):
    print(style * 12 + str(log_str) + style * 12)

def block(style="-",w=100,h=5):
    for _ in range(h):
        print(style*w)

