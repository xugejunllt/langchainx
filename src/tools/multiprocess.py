import multiprocessing
import os


def getProcessInfo():
    # 获取当前进程的ID
    pid = os.getpid()

    # 获取当前进程的名称
    # 在Unix系统上，可以通过os.readlink获取进程名称
    # 在Windows系统上，可以使用os.popen获取进程名称
    # if os.name == 'posix':
    #     proc_name = os.readlink(f'/proc/{pid}/exe')  # Unix系统
    # else:
    #     # Windows系统
    #     proc_name = os.path.basename(os.popen('tasklist /FI "PID eq {pid}" /FO TABLE').read().split('\n')[1].split()[0])

    print(f"Process ID: {pid}")
    # print(f"Process Name: {proc_name}")
    return pid


def worker():
    """子进程要执行的任务"""
    print('Worker')
    name = getProcessInfo()
    print(f"子进程id:{name}")


if __name__ == '__main__':
    # 创建子进程
    p = multiprocessing.Process(target=worker)
    # 启动子进程
    p.start()
    name = getProcessInfo()
    print(f"主进程id:{name}")
    # 等待子进程结束
    p.join()
