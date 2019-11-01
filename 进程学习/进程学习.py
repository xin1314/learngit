from multiprocessing import Process

def test(args):
    print("我是子进程",args)

def main():
    print("我是主进程")
    p = Process(target=test, args=(1, ))  # 实例化Process进程类
    p.start()
    print("主进程结束")

if __name__ == "__main__":
    main()