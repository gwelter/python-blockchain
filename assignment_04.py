import functools

def print_args(args):
    for a in args:
        print(a)


def proxy_function(function, *args):
    return function(args)


proxy_function(print_args, 1,3,4,5)
proxy_function(lambda args: print(args), 1,2,3,4,5)