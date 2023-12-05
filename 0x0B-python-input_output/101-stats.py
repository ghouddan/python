#!/usr/bin/python3

"""
A script that reads stdin line by line and computes metrics.
"""

import sys


def printStats(statusCodes, fileSize):
    """
    Prints stats.

    Arguments:
        statusCodes {dict} -- dictionary of status codes.
        fileSize {int} -- file size.
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    statusCodes = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    fileSize = 0
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            splitLine = line.split()
            try:
                fileSize += int(splitLine[-1])
            except (ValueError, IndexError):
                pass
            try:
                statusCodes[splitLine[-2]] += 1
            except (KeyError, IndexError):
                pass
            if count % 10 == 0:
                printStats(statusCodes, fileSize)
        printStats(statusCodes, fileSize)
    except KeyboardInterrupt:
        printStats(statusCodes, fileSize)
        raise
