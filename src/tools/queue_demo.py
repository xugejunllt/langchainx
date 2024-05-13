from multiprocessing import Process, Queue


def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()

    for i in range(10):
        q.put(i)

    q.put(None)
    p.join()
