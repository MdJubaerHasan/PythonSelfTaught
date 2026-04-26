import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

# 1. This is our heavy math task. Notice it is a NORMAL function, not async!
def calculate_volume():
    print("🥔 Starting intense math in a separate process...")
    time.sleep(5)  # Simulating heavy, non-stop CPU calculation
    return 42.5

async def make_sandwich():
    print("🥪 Making a quick sandwich...")
    await asyncio.sleep(1)
    print("🥪 Sandwich is done!")

async def main():
    # 2. We hire our separate kitchen (Process Pool)
    with ProcessPoolExecutor() as separate_kitchen:
        # 3. We get our current manager
        loop = asyncio.get_running_loop()

        print("Starting dinner prep...")

        # 4. We hand the math task to the separate kitchen and 'await' the delivery driver
        math_task = loop.run_in_executor(separate_kitchen, calculate_volume)

        # 5. While the separate kitchen does the math, our main chef makes the sandwich!
        await make_sandwich()

        # 6. Finally, we wait for the math to come back
        volume = await math_task
        print(f"The potato volume is: {volume}")


if __name__ == "__main__":
    asyncio.run(main())