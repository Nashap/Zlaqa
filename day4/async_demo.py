'''Build an async function with asyncio for parallel API calls.'''
import asyncio

async def get_users():
    print("Fetching users..")
    await asyncio.sleep(1)
    print("Users fetched")
    return "Users"

async def get_products():
    print("Fetching products..")
    await asyncio.sleep(1)
    print("Products fetched")
    return "Products"

async def get_orders():
    print("Fetching orders..")
    await asyncio.sleep(1)
    print("Orders fetched")
    return "Orders"

async def main():
    """Run all API calls concurrently"""
    results = await asyncio.gather(
        get_users(),
        get_products(),
        get_orders()
    )

    print("\nResults:")
    print(results)

asyncio.run(main())