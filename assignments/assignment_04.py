def function(*args):
    for arg in args:
        print(str(arg))


def proxy_function(function, *args):
    function(*args)


proxy_function(function, 10, 5, 6)
proxy_function(lambda *args: print(args), 25, 26)