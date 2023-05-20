import asyncio
import time


async def fun1():
    print("Molia最美")
    await asyncio.sleep(3)
    print("Molia最美")

async def fun2():
    print("pamdol最美")
    await asyncio.sleep(2)
    print("pamdol最美")

async def fun3():
    print("nami最美")
    await asyncio.sleep(4)
    print("nami最美")

if __name__ == '__main__':
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()
    tesk = [f1, f2, f3]
    t1 = time.time()
    asyncio.run(asyncio.wait(tesk))
    t2 = time.time()
    print(t2-t1)