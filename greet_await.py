import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}!")


async def main():
    print("Starting main coroutine...")
    await greet("Alice")
    await greet("Bob")
    print("Main coroutine finished")

if __name__ == "__main__":
    asyncio.run(main())
