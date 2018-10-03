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

    def get_json(self, target):
        response = requests.get(f"{self.url}{target}", verify=False, headers=HEADER)
        if response.status_code == 200:
            raw_data = response.json()
            parse_data = [row for row in raw_data["teams"]]
            teams_data = [dict(self.unpack_json(item)) for item in parse_data]
            return teams_data
        else:
            return "ERROR: %s" % response.text

    def unpack_json(self, data, *parent):
        for k, v in data.items():
            print(k, v)
            if isinstance(v, dict):
                yield from self.unpack_json(v, k)
            if isinstance(v, list):
                for sub in v:
                    print(f"list: {v}\n"
                          f"unpacked: {sub}")
                    yield from self.unpack_json(sub, k)
            elif parent:
                yield (f"{parent[0]}_{k}"), v
            elif not parent:
                yield k, v

    def team_data(self):
        return self.get_json("teams")

    def team_roster(self):
        return self.get_json("teams?expand=team.roster")

    def team_stats(self):
        return self.get_json("teams?expand=team.stats&expand=team.roster")


class Team:

    def __init__(self, team):
        print(team)
        for k, v in team.items():
            setattr(self, k, v)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_teamName(self):
        return self.teamName

    def get_abbreviation(self):
        return self.abbreviation

    def get_roster(self):
        return self.roster


class Player:
    pass


def main():

    #team_data = WebScrape().team_data()
    #print(team_data)
    #team_list = [Team(team) for team in team_data]

    stats_data = WebScrape().team_stats()
    stat_list = [Team(team) for team in stats_data]
    for team in stat_list:
        print(team.get_roster())


    df = pd.DataFrame([vars(x) for x in stat_list])
    df.to_csv(f'teams.csv', index=False)


    '''
    for i in stats_list:
        for attr, value in i.__dict__.items():
            print(attr, value)
    '''


if __name__ == '__main__':
    main()
