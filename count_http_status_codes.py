#!/usr/bin/env python
"""count_http_status_codes.py

Count the http status codes from the Nginx access log provided in the argument.
If no path to log is provided then "/var/log/nginx/access.log" will be used.
Depending on environment this may need to be ran with root access.

Usage:
  count_http_status_codes.py [/path/to/nginx/access.log]

"""
import sys
import os.path
from collections import Counter


def check_for_file():
    """
    Check for the nginx log file which can be provided as an argument.
    If not provided it will use the local log file located in /var/log/nginx/

    Returns: string
    """
    if len(sys.argv) > 1:
        logfile = sys.argv[1]
    else:
        if os.path.exists("/var/log/nginx/access.log"):
            logfile = "/var/log/nginx/access.log"
        else:
            print "The nginx log file does not exsist in it\'s expected location"
            sys.exit(1)

    return logfile


def count_status_codes(logfile):
    """
    Counts the status codes and outputs the number of each unique status code.

    Args:
        logfile (string)
    """
    log_file = open(logfile)

    status_codes = []

    for line in log_file:
        split_line = line.split
        status_codes.append(split_line()[8])

    counter = Counter(status_codes)

    for codes in counter.items():
        print "There are {} occurenses of HTTP status code {}".format(codes[1],
                                                                      codes[0])

def main():
    logfile = check_for_file()
    count_status_codes(logfile)


if __name__ == '__main__':
    main()
