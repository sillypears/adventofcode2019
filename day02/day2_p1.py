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
        return f.read().split(',')

def solve(data, debug):
    d_len = len(data)
    total_ops = 0
    i_nn = data.index('99')
    if debug: print("99 in position ", i_nn)
    for x in range(0,i_nn):
        if x % 4 == 0:
            total_ops += 1
    if debug: print(f"Lines {total_ops}")
    for pos in range(0, d_len, 4):
        op = int(data[pos])
        if int(op) == 1:
            p1 = int(data[int(data[pos+1])]) 
            p2 = int(data[int(data[pos+2])]) 
            p3 = int(data[pos+3]) 
            v3 = data[p3]
            data[p3] = p1 + p2
            if debug: print(f"{pos} op {op} {p1} + {p2} = {p1+p2} into {v3}")
        if int(op) == 2:
            p1 = int(data[int(data[pos+1])]) 
            p2 = int(data[int(data[pos+2])]) 
            p3 = int(data[pos+3])
            v3 = data[p3]
            data[p3] = p1 * p2
            if debug: print(f"{pos} op {op} {p1} * {p2} = {p1*p2} into {v3}")
        if int(op) == 99:
            return data



def main():
    debug = True
    day = 2
    if os.path.exists("test_inputs"):
        data = get_test_inputs()
    else:
        data  = get_inputs(day)

    answer = solve(data, debug)
    print(','.join(str(n) for n in answer))

if __name__ == "__main__":
    sys.exit(main())