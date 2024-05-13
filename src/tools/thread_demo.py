import threading

# 定义全局变量
count = 0

# 定义线程锁
# lock = threading.Lock()


# 定义线程函数
def add():
    global count
    for i in range(100000):
        # 获取锁
        # lock.acquire()
        count += 1
        # 释放锁
        # lock.release()


# 创建多个线程
threads = []
for i in range(10):
    t = threading.Thread(target=add)
    threads.append(t)

# 启动线程
for t in threads:
    t.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()


# 输出结果
print(count)
