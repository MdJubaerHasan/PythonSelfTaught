import asyncio

# asynchronous function

async def boil_water():
    print("Putting water on stove...")

    # This is where we wait while user chops vegetables
    await asyncio.sleep(5)

    print("Water is now boiling")

    return "Hot water"

async def chop_veggies():

    await  asyncio.sleep(1)
    print("Starting to stop vegetables")

    await asyncio.sleep(2)

    print("Vegetables are chopped")

    return "Chopped veggies"

"""

boil_water() we can't just run this function, as it is not a regular function
async functions create a coroutine -> packaged up "to-do" item, waiting to be scheduled,
To execute an async function, We need Event Loop, which acts as an overseer of the "to-do" list
runs the tasks and handles pasuing and resuming

If you forget await, Python looks at asyncio.sleep(5),
creates a "sleep timer" object in memory, and then instantly moves
to the next line without actually waiting.
So, await is necessary to actually trigger the pause.

Here comes the Manager (Event Loop)
This starts the manager and tells it to run our coroutine


running them one after the other is copying synchronous programming

asyncio.run(boil_water())
asyncio.run(chop_veggies())

Instead, we run them together using asyncio.gather() for that we need a main function
"""


async def main():
    print("Starting dinner prep...")

    # gather() groups them and we 'await' the group
    result = await asyncio.gather(boil_water(), chop_veggies())

    print(result)

# asyncio.run(main()) # Uncomment and Run this for previous lesson

# Advanced Topic
"""
You want to start a slow-cooker soup that takes 8 hours. You definitely don't want to use await or gather right away,
because that would force your program to pause for 8 hours before you are allowed to make a quick sandwich for lunch.
You want to start the soup in the "background," immediately move on to making your sandwich, and check on the soup much later.
To do this, Python lets us schedule a coroutine to run independently using something called asyncio.create_task().
"""

async def make_soup():
    print("1. Starting the slow cooker...")
    await asyncio.sleep(80)
    return "Soup 🍲 "

async def make_sandwich():
    print("A. Making a quick sandwich...")
    await asyncio.sleep(5)
    print("Sandwich 🥪")

async def kitchen():
    # Here we start the soup task immediately
    soup_task = asyncio.create_task(make_soup())

    # Immediately move on to making sandwich
    await make_sandwich()

    print(".... hours passed ...")

    # 3. Now it is dinner time. We MUST wait for the soup to finish.
    # If it's already done, this moves on instantly. If not, it pauses here.

    final_soup = await soup_task

    print(f"Dinner is served: {final_soup}")

asyncio.run(kitchen())