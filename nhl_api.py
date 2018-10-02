import requests
import pandas as pd
# from constant_variables import TEAMS


# Spoof browser
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/39.0.2171.95 Safari/537.36'}


class WebScrape:

    def __init__(self):
        self.url = "https://statsapi.web.nhl.com/api/v1/"

    def get_data(self, target):
        response = requests.get(f"{self.url}{target}", verify=False, headers=HEADER)
        if response.status_code == 200:
            return response.json()
        else:
            return "ERROR: %s" % response.text


class Team:

    def __init__(self, team):
        #teams = WebScrape().get_data(tag)
        #a_list = [row for row in teams[tag]]
        #teams_list = [dict(unpack(item)) for item in a_list]
        #for team in teams_list:
        for k, v in team.items():
                print(object)
                setattr(self, k, v)

    def populate_team_data(self):
        teams = WebScrape().get_data("teams")
        a_list = [row for row in teams["teams"]]
        teams_list = [dict(unpack(item)) for item in a_list]
        master_list = []
        print(teams_list)
        for team in teams_list:
            print(team)
            master_list.append(Team(team))
        return master_list


class Player:
    pass

'''
def populate_team_data(tag):
    nhl = WebScrape()
    team = nhl.get_data(tag)
    raw_list = [row for row in team[tag]]
    team_list = [dict(unpack(item)) for item in raw_list]
    for team in team_list:
        print(team)
        Team(team)
'''

def create_dataframe(response, tag):
    """
    Take a dictionary of JSON objects and return them as a dataframe

    Parameters:
        response (dict): Response from requests.get()
        tag (str): Used to unpack the dictionary at a specific key(tag)

    Returns:
        df (DataFrame): Unpacked JSON object with headers in dataframe format
    """

    raw_list = [row for row in response[tag]]
    df_list = [dict(unpack(item)) for item in raw_list]
    df = pd.DataFrame(df_list)
    df.to_csv(f'{tag}.csv', index=False)
    return df


def unpack(data, *parent):
    """
    Take a nested dictionary and unpack the nested keys/values.  Pass forward the parent key when a level is unpacked
    and append to nested key to avoid duplicate key names.

    Parameters:
        data (dict): Individual dict entries from raw_list.  Some have nested dicts as children.
        *parent (str): Passed back via yield from to see if item was nested.  If so, append the parent key name to
                       the child key to avoid duplicate key names.

    Yields:
        k, v (str): Either yields back into itself if the value is a dict (nested) or yields a key/value pair.
    """

    for k, v in data.items():
        if isinstance(v, dict):
            yield from unpack(v, k)
        elif parent:
            yield (f"{parent[0]}_{k}"), v
        elif not parent:
            yield k, v


def main():
    #teams = Team("teams")
    #for a in teams:
    #    print(a.name, a.id, a.abbreviation)

    a = Team.populate_team_data("teams")
    print(a['name'])


if __name__ == '__main__':
    main()
