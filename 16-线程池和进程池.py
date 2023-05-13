# 线程池：一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度由线程池来完成

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(200):
        print(name,i)
        
if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")

    print("114514")