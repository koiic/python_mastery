""": Classic League
base_url =
Information for the ClassicLeague is taken from e.g. the following endpoint:
https://fantasy.premierleague.com/drf/leagues-classic-standings/1137
An example of what information a ClassicLeague contains is shown below:
"""
import asyncio

import aiohttp
from fpl import FPL


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login(email="ibraismail1990@gmail.com", password="Calory@20")
        classic_league = await fpl.get_classic_league(1137)
    print(classic_league)



""": Fixture

Information for the Fixture is taken from e.g. the following endpoints: 
base_url = https://fantasy.premierleague.com/api/fixtures/ 
https://fantasy.premierleague.com/api/fixtures/?event=1
An example of what information a ClassicLeague contains is shown below:
"""

async def fixture():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fixtures = await fpl.get_fixture(1)
    print(fixtures)



if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(fixture())
