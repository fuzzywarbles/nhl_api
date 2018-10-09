import requests
import json
import os
from itertools import chain, starmap
from collections import defaultdict
import pandas as pd
from constant_variables import *


def url_to_filename(url):
    no_ext = url.replace("/", "_").replace("?", "_")
    return f"{no_ext}.json"


def get_json(url):
    os.chdir(JSON_ROOT)
    filename = url_to_filename(url)

    if not os.path.exists(filename):
        print(f"{filename}.json does not exist.  Attempting to get: {URL_BASE}{url}\n")
        response = requests.get(f"{URL_BASE}{url}", verify=False, headers=HEADER)
        if response.status_code == 200:
            raw_data = response.json()
            with open(filename, "w") as write_file:
                json.dump(raw_data, write_file, sort_keys=True, indent=4)
        else:
            return "ERROR: %s" % response.text

    with open(filename) as f:
        raw_data = json.load(f)
        return raw_data


def parse_roster(team_id=None):

    # Specify team via id
    if team_id:
        url = f"teams/{team_id}/roster"
        filename = url_to_filename(url)
        raw_data = get_json(url)

        roster_list = (flatten_dict(item) for item in raw_data['roster'])

    # Every team
    else:
        url = f"teams?expand=team.roster"
        filename = url_to_filename(url)
        raw_data = get_json(url)

        roster_list = []

        for team in raw_data['teams']:

            team_names = dict((k, v) for k, v in team.items() if k == 'name')
            flat_roster = ([flatten_dict(x) for x in team['roster']['roster']])

            for player in flat_roster:

                player_dict = defaultdict(int, (("_".join(key), value) for (key, value) in player.items()))

                # Attach team name to player
                player_dict.update(team_names)

                # Player Stats
                stats = parse_player_stats(player_dict['person_id'])
                if isinstance(player_dict, dict):
                    player_dict.update(stats)
                    roster_list.append(player_dict)

    df = pd.DataFrame(roster_list)
    df.to_csv(f"{filename}_df.csv", index=False)


def parse_player_stats(player_id):
    url = f"people/{player_id}/stats?stats=statsSingleSeason&season=20182019"
    raw_data = get_json(url)
    tuples = dict((k, v) for i in raw_data['stats'] for x in i['splits'] for k, v in x['stat'].items())
    return tuples


def flatten_dict(dictionary):
    """Flatten a nested dictionary structure"""

    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        try:
            items = parent_value.items()
        except AttributeError:
            # parent_value was not a dict, no need to flatten
            yield (parent_key, parent_value)
        else:
            for key, value in items:
                yield (parent_key + (key,), value)

    # Put each key into a tuple to initiate building a tuple of subkeys
    dictionary = {(key,): value for key, value in dictionary.items()}

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break

    return dictionary


def main():

    parse_roster()


if __name__ == '__main__':
    main()
