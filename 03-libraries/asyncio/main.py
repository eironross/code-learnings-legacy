import asyncio

async def send_data(name: str):
    print(f"Sending data to: {name}")
    await asyncio.sleep(2)
    print(f"Sent the data to: {name}")

async def get_data():
    print("Fetching data..")
    await asyncio.sleep(2.5)
    print("Data Fetched...")
    return {
        "message": "Hi Mom!"
    }

async def main():
    data = await get_data()
    #await send_data(data.get("message")) # using this await in order will run the function in sync to fully use async
    await asyncio.gather(send_data("Eiron"), send_data("Aiah"))
    # Gather has no error handler, use .TaskGroup() since there a err ahandler
    
async def task():
    task = asyncio.create_task(
        get_data()
    )

    # task.cancel()
    
    try:
        await asyncio.wait_for(task, timeout=5)
        
    except asyncio.CancelledError:
        print(f"Cancelled: Request was cancelled...")
    except asyncio.TimeoutError:
        print(f"Timeout: Request was timeout...")

if __name__ == "__main__":
    result = asyncio.run(get_data())
    print(result)