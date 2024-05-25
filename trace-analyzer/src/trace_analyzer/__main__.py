async def main():
    """Main loop"""


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    print("Exited main loop...")
    raise EOFError("Main loop ended without throwin exceptions.")