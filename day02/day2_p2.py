import requests, os, sys
import copy

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

def solve(adata, noun, verb, debug):
    data = copy.deepcopy(adata)
    data[1]  = noun
    data[2] = verb

    d_len = len(data)
    total_ops = 0
    i_nn = data.index('99')
    for x in range(0,i_nn):
        if x % 4 == 0:
            total_ops += 1
    for pos in range(0, d_len, 4):
        op = int(data[pos])
        if int(op) == 1:
            try:
                p1 = int(data[int(data[pos+1])]) 
                p2 = int(data[int(data[pos+2])]) 
                p3 = int(data[pos+3]) 
                v3 = data[p3]
                data[p3] = p1 + p2
                if data[p3] == 19690720:
                    d1 = data[1]
                    d2 = data[2]
                    print(f"noun: {d1} verb: {d2} op: {op}")
            except Exception as e:
                pass # print(f"Couldn't process {p3}: {e}")
        if int(op) == 2:
            try:
                p1 = int(data[int(data[pos+1])]) 
                p2 = int(data[int(data[pos+2])]) 
                p3 = int(data[pos+3])
                v3 = data[p3]
                data[p3] = p1 * p2
                if data[p3] == 19690720:
                    d1 = data[1]
                    d2 = data[2]
                    print(f"noun: {d1} verb: {d2} op: {op}")
            except Exception as e:
                pass#print(f"Couldn't process {p3}: {e}")
        if int(op) == 99:
            return data

def main():
    debug = True
    day = 2
    if os.path.exists("test_inputs"):
        data = get_test_inputs()
    else:
        data  = get_inputs(day)

    for x in range(0,99):
        for y in range(0,99):
            answer = solve(data, x, y, debug)
            if int(answer[0]) == 19690720:
                print("answer: {}".format((100 * answer[1]) +  answer[2]))
                sys.exit()

if __name__ == "__main__":
    sys.exit(main())