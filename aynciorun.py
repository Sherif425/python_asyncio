import asyncio
import time

async def task_a():
    print(f"[{time.strftime('%X')}] Task A: Starting...")
    await asyncio.sleep(2)
    print(f"[{time.strftime('%X')}] Task A: Finished!")

async def task_b():
    print(f"[{time.strftime('%X')}] Task B: Starting...")
    await asyncio.sleep(1)
    print(f"[{time.strftime('%X')}] Task B: Finished!")

async def main_sequential():
    print(f"[{time.strftime('%X')}] Main Sequential: Program starts.")
    await task_a() # Finishes after ~2 seconds
    await task_b() # Starts after task_a, finishes after ~1 more second
    print(f"[{time.strftime('%X')}] Main Sequential: Program ends.")

if __name__ == "__main__":
    print("--- Running Sequential Example ---")
    asyncio.run(main_sequential())


# import asyncio
# import time

# async def task_a():
#     print(f"[{time.strftime('%X')}] Task A: Starting...")
#     await asyncio.sleep(2) # Simulate 2 seconds of I/O bound work
#     print(f"[{time.strftime('%X')}] Task A: Finished!")

# async def task_b():
#     print(f"[{time.strftime('%X')}] Task B: Starting...")
#     await asyncio.sleep(1) # Simulate 1 second of I/O bound work
#     print(f"[{time.strftime('%X')}] Task B: Finished!")

# async def main():
#     print(f"[{time.strftime('%X')}] Main: Program starts.")
#     await task_a() # Main waits for task_a to complete
#     await task_b() # Main waits for task_b to complete
#     print(f"[{time.strftime('%X')}] Main: Program ends.")

# if __name__ == "__main__":
#     asyncio.run(main())