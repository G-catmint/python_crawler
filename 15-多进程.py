# 不建议使用多进程，相较于多线程，多进程更加浪费资源

from multiprocessing import Process

class MyProcess(Process):
    def run(self):
        for i in range(10000000):
            print("run",i)

if __name__ == '__main__':
    m = MyProcess()
    m.run()
    m.start()
    for i in range(10000000):
        print("main",i)