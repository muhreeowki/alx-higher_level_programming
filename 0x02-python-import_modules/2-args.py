#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    s = "" if argc == 1 else "s"
    print("{} argument{}".format(argc if argc > 0 else 0, s),
          end=":\n" if argc > 0 else ".\n")
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
