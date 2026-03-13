import httpx
from selectolax.parser import HTMLParser

BASE_URL = "https://www.leboncoin.fr/recherche"


async def fethch_page(query: str = "velo", page: int = 1) -> list[dict]:
    params = {
        "text": query,
        "page": page,
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params, headers=headers)

    tree = HTMLParser(response.text)

    listings = []

    # for node in tree.css("a[data-qa-id='aditem_container']"):
    #     title = node.css_first("p[data-qa-id='aditem_title']")
    #     price = node.css_first("span[data-qa-id='aditem_price']")

    #     if not title or not price:
    #         continue

    #     listings.append(
    #         {
    #             "title": title.text(strip=True),
    #             "price": price.text(strip=True),
    #             "marketplace": "leboncoin",
    #         }
    #     )

    for node in tree.css("a"):
        title = node.text(strip=True)
        if "velo" in title.lower():
            listings.append(
                {
                    "title": title,
                    "marketplace": "leboncoin",
                }
            )

    return listings
