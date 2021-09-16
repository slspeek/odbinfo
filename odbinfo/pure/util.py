"Utilities"
import time
from functools import wraps


def timed(mesg, indent=0, arg=None, name=True):
    "Timing decorator"
    def decorate(func):

        def message(args):
            result = indent * " " + mesg
            if not arg is None:
                result += " on "
                if name:
                    result += args[arg].name
                else:
                    result += args[arg]
            return result

        @wraps(func)
        def wrapper(*args, **kwargs):
            if arg is None:
                print(message(args) + ' started ')
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(message(args) + ' finished in %.2f seconds ' %
                  (end_time-start_time))

            return result
        return wrapper
    return decorate
