import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(1, 6):
        await asyncio.sleep(10-power)
        print(f'Силач {name} поднял {ball_number} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Biceps', 9))
    task2 = asyncio.create_task(start_strongman('Baby', 5))
    task3 = asyncio.create_task(start_strongman('Sweet', 7))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())