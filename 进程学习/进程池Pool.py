from multiprocessing import Pool
import time
import os

def task(name):
    print("子进程（%s）开始执行task%s, 父进程为（%s）" % (os.getpid(), name, os.getppid()))
    time.sleep(1)

if __name__ == "__main__":
    print("父进程（%s）开始执行" %(os.getpid()))
    p = Pool(3)  # 定义一个进程池，最大进程数为3
    for i in range(10):
        p.apply_async(task, args=(i, ))  # 使用非阻塞方式调用task()函数
    print("等待所有子进程结束。。。")
    p.close()  # 关闭进程池，关闭后p不再接受新的请求
    p.join()  # 等待子进程结束
    print("子进程结束")
