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

async def main_concurrent():
    print(f"[{time.strftime('%X')}] Main Concurrent: Program starts.")

    task1 = asyncio.create_task(task_a())
    task2 = asyncio.create_task(task_b())

    # These await calls will wait for the *completion* of the tasks,
    # but the tasks themselves were started concurrently.
    await task1
    await task2

    print(f"[{time.strftime('%X')}] Main Concurrent: Program ends.")

if __name__ == "__main__":
    print("\n--- Running Concurrent Example ---")
    asyncio.run(main_concurrent())



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

#     # Create tasks. These start running "in the background"
#     # as soon as the Event Loop gets a chance.
#     task1 = asyncio.create_task(task_a())
#     task2 = asyncio.create_task(task_b())

#     # Now, await them to ensure the main program doesn't exit
#     # before they are done. This is where main waits for BOTH
#     # tasks to complete, but they run concurrently with each other.
#     await task1
#     await task2

#     print(f"[{time.strftime('%X')}] Main: Program ends.")

# if __name__ == "__main__":
#     asyncio.run(main())