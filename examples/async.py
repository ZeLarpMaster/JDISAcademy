import asyncio
import random


async def task(num):
    print(f"in > {num}")
    await asyncio.sleep(random.random() / 5)
    print(f"out< {num}")


async def main():
    print("Initializing futures")
    futs = [asyncio.ensure_future(task(num)) for num in range(5)]
    print("Waiting for futures")
    await asyncio.wait(futs)
    print("Done!")


print("Starting...")
asyncio.run(main())
print("Exiting...")


# Pour plus d'information: https://docs.python.org/3.8/library/asyncio.html
