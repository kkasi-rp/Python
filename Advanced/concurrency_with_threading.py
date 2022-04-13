
import time
import concurrent.futures

def do_something(name):
    print(f'starting thread {name}')
    time.sleep(2)
    print(f'ending thread {name}')
    if(name==1):
        raise ValueError
    return name

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(do_something, input) for input in range(3)]
    for future in futures:
        try:
            print(future.result())
        except Exception as err:
            print(f'Exception Occurred : {err!r}')

