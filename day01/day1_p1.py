import requests, os, sys
import math

from auth import AUTH

def get_inputs(day):
    """ Gets the daily input given the day 

    Parameters:
    day [{int}] -- Integer value of the day

    Returns:
    str -- String value from the input requested

    """
    url = "https://adventofcode.com/2019/day/{}/input".format(day)
    cookies = dict(session=AUTH)
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.text.splitlines()
    else:
        print("Couldn't get inputs, update cookie")
        sys.exit(1)

def get_test_inputs():
    with open('test_inputs', 'r') as f:
        return f.read().splitlines()

def solve(data):
    try:
        data = int(data.rstrip())
    except Exception as e:
        print(data, e)
        return 0

    return math.floor(data / 3) - 2

def main():
    debug = True
    day = 1
    if os.path.exists("test_inputs"):
        data = get_test_inputs()
    else:
        data  = get_inputs(day)

    total = 0

    for x in data:
        total += solve(x)

    print(total)

if __name__ == "__main__":
    sys.exit(main())