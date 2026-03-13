import asyncio
import json
from pathlib import Path

from app.collectors.leboncoin import fethch_page

DATA_FILE = Path("data/listings.json")


async def main():
    listings = await fethch_page()
    print(f"Fetched {len(listings)} listings")

    DATA_FILE.parent.mkdir(exist_ok=True)
    existing_listings = []

    if DATA_FILE.exists() and DATA_FILE.stat().st_size > 0:
        with open(DATA_FILE) as f:
            existing_listings = json.load(f)

    existing_listings.extend(listings)

    with open(DATA_FILE, "w") as f:
        json.dump(existing_listings, f, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
