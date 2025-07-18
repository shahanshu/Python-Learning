import asyncio

async def f1():
    await asyncio.sleep(4)
    print("f1 func")

async def f2():
    await asyncio.sleep(2)
    print("f2 function taking time")


async def main():
    t1=asyncio.create_task(f1())
    t2=asyncio.create_task(f2())

    await(t1)
    await(t2)

asyncio.run(main())
