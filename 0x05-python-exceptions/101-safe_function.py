#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        result = None
    finally:
        return (result)
