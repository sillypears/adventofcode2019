import requests, os, sys

sys.path.append('..')
from auth import AUTH

def get_inputs(day):
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

def get_dir(i):
    dir = i[0]
    try:
        num = int(i[1::])
    except:
        print(f"What the heck it broke")
        sys.exit()
    return dir, num

def get_max(w):
    m = 0
    for x in w:
        d, n = get_dir(x)
        m = n if n > m else m
    return m

def move(spot, d):
    n_spot = spot

    if d.upper() == "U":
        n_spot = (spot[0], spot[1] + 1)
    if d.upper() == "D":
        n_spot = (spot[0], spot[1] - 1)
    if d.upper() == "R":
        n_spot = (spot[0] + 1, spot[1])
    if d.upper() == "L":
        n_spot = (spot[0] - 1, spot[1])

    return n_spot


def solve(w1, w2, debug):
    matrix = {}
    max1 = get_max(w1)
    max2 = get_max(w2)

    spot1 = (0,0)
    steps = 0
    for direc in w1:
        d, n = get_dir(direc)
        for x in range(n):
            steps += 1
            spot1 = move(spot1, d)
            if spot1 not in matrix:
                matrix[spot1] = steps

    spot2 = (0,0)
    steps = 0
    small_dist = -10
    for direc in w2:
        d, n = get_dir(direc)
        for x in range(n):
            steps += 1
            spot2 = move(spot2, d)
            if spot2 in matrix:
                print("Crossing streams")
                dist = matrix[spot2] + steps
                if dist < small_dist or small_dist == -10:
                    small_dist = dist

    print(small_dist)

def main():
    debug = True
    day = 0
    if os.path.exists("test_inputs"):
        data = get_test_inputs()
    else:
        data  = get_inputs(day)
    wire1 = data[0].split(',')
    wire2 = data[1].split(',')
    solve(wire1, wire2, debug)

    if debug: print(wire1, wire2)
if __name__ == "__main__":
    sys.exit(main())