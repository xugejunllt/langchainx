import concurrent.futures
import time


def worker(num):
    print(f"Thread-{num} started\n")
    time.sleep(1)
    print(f"Thread-{num} finished")


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(5):
            executor.submit(worker, i)
