#!/usr/bin/env python3

"""
Stanford CS106A flights Project
"""

import sys


def parse_flights(text):
    """
    Given text with lines of flight data,
    returns flights dict.
    More Doctests TBD
    >>> parse_flights('sfo,1,2\\nsfo,3,4\\n')
    {'sfo': [(1, 2), (3, 4)]}
    >>> parse_flights('sfo,3,4\\nmfr,5,6\\nsfo,1,2\\n')
    {'sfo': [(3, 4), (1, 2)], 'mfr': [(5, 6)]}
    >>> parse_flights('sfo,10,20\\nmfr,1,1\\ndls,9,9\\n')
    {'sfo': [(10, 20)], 'mfr': [(1, 1)], 'dls': [(9, 9)]}
    """
    flights = {}
    broken = text.splitlines()
    previous = ''
    for info in broken:
        for i in range(len(info)):
            if info[i] == ',' and previous.isalpha():
                comma1 = i
                city = info[:i]
                if city not in flights:
                    flights[city] = []
                flight_info = flights[city]
            if info[i] == ',' and previous.isdigit():
                comma2 = i
                (time, people) = (int(info[comma1 + 1:comma2]), int(info[comma2 + 1:]))
                if (time, people) not in flight_info:
                    flight_info.append((time, people))
            previous = info[i]
    return flights


def read_sched(filename):
    """
    (provided)
    Returns flights dict parsed from file.
    """
    with open(filename, 'r') as f:
        text = f.read()
    return parse_flights(text)


def main():
    # (provided)
    args = sys.argv[1:]
    flights = read_sched(args[0])
    print(flights)


if __name__ == '__main__':
    main()
