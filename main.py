import aiohttp
import asyncio
from datetime import datetime, timedelta


async def main():

    limit = datetime.date(datetime.today()) - timedelta(days=10)
    date = datetime.date(datetime.strptime(input(f'Enter the date (DD.MM.YYYY) by which to display the exchange rate (limit: {limit.strftime("%d.%m.%Y")}): '), '%d.%m.%Y'))
    if date < limit:
        print ("You entered a date that exceeds the allowable limit")
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={datetime.strftime(date, "%d.%m.%Y")}') as response:
                result = await response.json()
                return result


if __name__ == "__main__":
    r = asyncio.run(main())
    print(r)