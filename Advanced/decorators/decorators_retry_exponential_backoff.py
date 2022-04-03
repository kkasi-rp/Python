# delayed retry functionality with exponential backoff using decorators

import logging
import random
import time

# * in paramter indicates all params after it are only keyword params
def retry(exceptions_to_handle=Exception, log_handler=None, *, max_attempts=5, initial_delay=0.5, backoff_factor=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = log_handler.warning if log_handler else print
            current_attempt, delay = 0, initial_delay # copying to local scope as we are updating value 
            while current_attempt <= max_attempts:
                try:
                    logger(f'Calling : {func.__name__}')
                    return func(*args, **kwargs)
                except exceptions_to_handle as err:
                    # convert err to raw format
                    logger(f'Exception : {err!r}')
                    current_attempt += 1
                    if current_attempt<=max_attempts:
                        logger(f'Retry : {current_attempt} After : {delay} sec')
                        time.sleep(delay)
                        delay *= backoff_factor
        return wrapper
    return decorator

# Driver code 
log_handler = logging.Logger(__name__)

# can pass any tuple of exceptions (ValueError, TimeoutError)
exceptions = (RuntimeError, ZeroDivisionError, ValueError)

@retry(exceptions, log_handler, max_attempts=3, initial_delay=1, backoff_factor=2)
def raise_random_exception():
    raise exceptions[random.randint(0, 2)]

raise_random_exception()