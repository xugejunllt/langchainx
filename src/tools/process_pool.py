import multiprocessing


def worker(num):
    """进程池中的任务"""
    print('Worker %d is running' % num)


if __name__ == '__main__':
    # 创建进程池，池中有3个进程
    pool = multiprocessing.Pool(processes=3)
    # 向进程池中添加任务
    for i in range(5):
        pool.apply_async(worker, args=(i,))
    # 关闭进程池，不再接受新的任务
    pool.close()
    # 等待所有任务完成
    pool.join()
    print('All workers done.')
