#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if(args <= 1):
        print("{} arguments.".format(args - 1))
    elif(args == 2):
        print("{} argument:".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))
    for x in range(1, args):
        print("{}: {}".format(x, sys.argv[x]))
