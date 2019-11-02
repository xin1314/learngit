from multiprocessing import Process
import os
import time

# 继承Process类
class SubProcess(Process):
    def __init__(self, args, name=''):
        # 由于Process类本身也有__init__初始化方法，这个子类相当于重写了父类的这个方法
        # Process.__init__(self)  # 调用父类的初始化方法
        super().__init__()
        self.args = args  # 接收sleep长度参数
        if name:  # 判断传递的那么参数是否存在
            self.name = name  # 如果传递参数那么，则为子进程创建那么属性，否则使用默认属性

    def run(self):  # 重写Process类的run()方法
        print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()  # 计时开始
        time.sleep(self.args)
        t_end = time.time()  # 计时结束
        print("子进程（%s）执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))

if __name__ == "__main__":
    print("---父进程开始执行---")
    print("父进程PID： %s" % (os.getpid()))
    p1 = SubProcess(args=1)
    p2 = SubProcess(name="mrsoft", args=2)
    # 对一个不包含target属性的Process类执行start()，就会运行这个类中的run()方法
    p1.start()
    p2.start()

    # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    # 输出p1和p2进程的别名和PID
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("---等待子进程---")
    p1.join()
    p2.join()
    print("---父进程执行结束---")

    print(Process.mro())
    print(SubProcess.mro())
