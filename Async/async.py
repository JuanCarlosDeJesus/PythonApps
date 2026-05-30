# AsyncIO and Asynchronous
import asyncio

# async def main():
#     print("A")
#     await asyncio.sleep(1)  # forces python to wait until this line completes before proceeding
#     print("B")

# async def other_func():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")

# asyncio.run(main())

# await calls and runs another func

# async def main():
#     print("A")
#     await other_func()  # forces python to wait until this line completes before proceeding
#     print("B")

# async def other_func():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")

# asyncio.run(main())

# runs both func

# async def main():
#     task = asyncio.create_task(other_func())
#     print("A")
#     await asyncio.sleep(1)
#     print("B")
#     await task
    

# async def other_func():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")

# asyncio.run(main())

# await task - forces python to complete the task or func first before proceeding
# async def main():
#     task = asyncio.create_task(other_func())
#     await task
#     print("A")
#     await asyncio.sleep(1)
#     print("B")
#     await task
    

# async def other_func():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")

# asyncio.run(main())

# async returns
async def main():
    task = asyncio.create_task(other_func())
    print("A")
    await asyncio.sleep(5)
    print("B")
    return_value = await task
    print(f"The return value was {return_value}")
    

async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())