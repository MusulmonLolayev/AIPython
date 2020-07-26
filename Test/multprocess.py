from concurrent.futures import ThreadPoolExecutor
import numpy as np
from time import sleep, time


def test(start, finish, a, b):
    for i in range(start, finish):
        sleep(1)
        a += start
        print(i)

def main():
    x = np.array([[1, 2], [2, 3]])
    with ThreadPoolExecutor(max_workers=10) as executor:
        future = executor.submit(test, 0, 3, x, 2)
        future = executor.submit(test, 3, 6, x, 2)
        future = executor.submit(test, 6, 9, x, 2)
        future = executor.submit(test, 9, 12, x, 2)

    print(x)
if __name__ == '__main__':
    start = time()
    main()
    done = time()

    print(done - start)