import sys

import aiohttp
import asyncio

from colorama import Fore
from fpl import FPL
from fpl.utils import team_converter
from prettytable import PrettyTable


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        player_with_json = await fpl.get_player(302, return_json=True)
        player = await fpl.get_player(302)
        print(player)  # get basic player info

        print(player.points_per_game)  # get player point per game
        print(player.total_points)  # get player total point
        print(player_with_json)  # get basic player info
        print(player_with_json['chance_of_playing_next_round'])  # get basic player info


async def my_team(user_id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login(email="ibraismail1990@gmail.com", password="Calory@20")
        user = await fpl.get_user(user_id)
        team = await user.get_team()

    print(team)


async def top_performers():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    top_performers = sorted(players, key=lambda x: x.goals_scored + x.assists, reverse=True)

    player_table = PrettyTable()
    player_table.field_names = ["Player", "£", "G", "A", "G + A"]
    player_table.align["Playwer"] = "1"

    for player in top_performers[:10]:
        goals = player.goals_scored
        assists = player.assists
        player_table.add_row([player.web_name, f"£{player.now_cost / 10}", goals, assists, goals + assists])

    print(player_table)


async def new_fdr():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fdr = await fpl.FDR()

    fdr_table = PrettyTable()
    fdr_table.field_names = [
        "Team", "All (H)", "All (A)", "GK (H)", "GK (A)", "DEF (H)", "DEF (A)",
        "MID (H)", "MID (A)", "FWD (H)", "FWD (A)"
    ]

    for team, position in fdr.items():
        row = [team]
        for difficulties in position.values():
            for location in ["H", "A"]:
                if difficulties[location] == 5.0:
                    row.append(Fore.RED + "5.0" + Fore.RESET)
                elif difficulties[location] == 1.0:
                    row.append(Fore.GREEN + "1.0" + Fore.RESET)
                else:
                    row.append(f"{difficulties[location]:.2f}")

        fdr_table.add_row(row)

    fdr_table.align["Team"] = "1"
    print(fdr_table)


def get_game_week_score(player, game_week):
    gameweek_history = next(history for history in player.history if history['round'] == game_week)
    return gameweek_history["total_points"]


def get_game_week_opponent(player, game_week):
    game_week_history = next(history for history in player.history if history['round'] == game_week)
    return f"{team_converter(game_week_history['opponent_team'])}", f"{'H' if game_week_history['was_home'] else 'A'}"


def get_point_difference(player_a, player_b, gameweek):
    if player_a == player_b:
        return 0
    history_a = next(history for history in player_a.history
                     if history["round"] == gameweek)
    history_b = next(history for history in player_b.history
                     if history["round"] == gameweek)
    return history_a["total_points"] - history_b["total_points"]


async def optimal_captain_selection(user_id):
    player_table = PrettyTable()
    player_table.field_names = ["Gameweek", "Captain", "Top scorer", "Δ"]
    player_table.align = "r"
    total_difference = 0

    async with aiohttp.ClientSession() as session:
        fpl = FPL(session=session)
        user = await fpl.get_user(user_id)
        picks = await user.get_picks()
        print(picks, "+---")
        # for i, elements in enumerate(picks):
        for key,value in picks.items():
            # print(key, value,"+++>>")
            game_week = key + 1
            # print((player for player in elements if player["is_captain"]))
            captain_id = next(player for player in value if player["is_captain"])["element"]
            players = await fpl.get_players([player["element"] for player in value], include_summary=True)
            captain = next(player for player in players if player.id == captain_id)
            top_scorer = max(players, key=lambda x: get_game_week_score(x, game_week))
            point_difference = get_point_difference(captain, top_scorer, game_week)

            player_table.add_row([
                game_week,
                (f"{captain.web_name} - "
                 f"{get_game_week_score(captain, game_week)} points vs. "
                 f"{get_game_week_opponent(captain, game_week)}"),
                (f"{top_scorer.web_name} - "
                 f"{get_game_week_score(top_scorer, game_week)} points vs. "
                 f"{get_game_week_opponent(top_scorer, game_week)}"),
                point_difference
            ])
            total_difference += point_difference

    print(player_table)
    print(f"Total point difference is {abs(total_difference)} points!")



if __name__ == "__main__":
    if sys.version_info >= (3, 7):
        # Python 3.7+
        # asyncio.run(main())
        # asyncio.run(my_team(8819755))
        # asyncio.run(top_performers())
        asyncio.run(new_fdr())
        asyncio.run(optimal_captain_selection(3808385))
    else:
        # Python 3.6
        print("I'm using python 3.6")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.run_until_complete(my_team(8819755))
        loop.run_until_complete(top_performers())
        loop.run_until_complete(new_fdr())
