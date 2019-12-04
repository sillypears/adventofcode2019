import requests, os, sys

sys.path.append('..')
from auth import AUTH

def get_inputs(day):
    url = "https://adventofcode.com/2019/day/{}/input".format(day)
    cookies = dict(session=AUTH)
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.text
    else:
        print("Couldn't get inputs, update cookie")
        sys.exit(1)

def get_test_inputs():
    with open('test_inputs', 'r') as f:
        return f.read()

def solve(r1, r2, debug):
    found_passwords = 0
    for v in range(r1, r2+1):

        found_same = False
        c = 0
        last_n = -1
        valid = [0,0,0,0,0,0]
        for n in str(v):
            n = int(n)
            # print(last_n, n)    
            if last_n == n:
                valid[c] = 1
                found_same = True
            if last_n < n:
                valid[c] = 1
            c += 1
            last_n = n
        # print(v, valid, found_same)
        if 0 not in valid and found_same:
            found_passwords += 1
            if debug: print(v)
    return found_passwords

def main():
    debug = False
    day = 4
    if os.path.exists("test_inputs"):
        data = get_test_inputs()
    else:
        data  = get_inputs(day)

    if debug: print(data)

    r1, r2 = data.split('-')
    if (r1 > r2): sys.exit("This is bad")
    f = solve(int(r1), int(r2), debug)
    print(f"Found {f} valid answers in range {r1}-{r2}")
if __name__ == "__main__":
    sys.exit(main())