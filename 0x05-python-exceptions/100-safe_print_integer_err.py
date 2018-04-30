#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}".format(err))
        return(False)
