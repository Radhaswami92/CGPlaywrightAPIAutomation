import asyncio
import time
from asyncio import tasks


def task(name):
    print(f"starting: {name}")
    time.sleep(2)
    print(f"finishing: {name}")

task("Jeet")
task("Biswas")


async def task(name):
    print(f"starting: {name}")
    await asyncio.sleep(2)
    print(f"finishing: {name}")

async def main():
    await asyncio.gather( task( "Jeet" ), task ( "Biswas" ))

asyncio.run( main() )