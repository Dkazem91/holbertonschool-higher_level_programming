#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return(fct(*args))
    except:
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return(None)
