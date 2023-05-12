# 进程，线程
# 进程是资源单位 每一个进程至少有一个线程
# 线程是执行单位

from threading import Thread  # 创造多线程的包

# 1.创造线程的第一个写法

# def func():
#     for i in range(1000):
#         print("func",i)
# if __name__ == '__main__':
#     t = Thread(target=func)     # 创造线程 并给线程安排func的任务
#     # 开始线程
#     t.start()       # 分配出一个多的线程 而第二条线程什么时候1开始运行 由cpu决定
#                     # 从而使两个线程在输出中出现混杂的情况
#     for i in range(1000):
#         print("main",i)


# 2.创造线程的第二种写法
class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print("run",i)

if __name__ == '__main__':
    m = MyThread()
    m.run()
    m.start()
    for i in range(1000):
        print("main",i)