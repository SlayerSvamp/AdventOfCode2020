import time


def timeit(display_name=None, /):
    def decorator(method):
        _display_name = display_name or method.__name__

        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            if 'log_time' in kw:
                name = kw.get('log_name', method.__name__.upper())
                kw['log_time'][name] = int((te - ts) * 1000)
            else:
                print(f'{_display_name}: {(te - ts) * 1000:.2f} ms')
            return result
        return timed
    return decorator


if __name__ == '__main__':
    @timeit('name')
    def test():
        pass

    test()
