import requests
import pandas as pd
# from constant_variables import TEAMS


# Spoof browser
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/39.0.2171.95 Safari/537.36'}


class WebScrape(object):

    def __init__(self):
        self.url = f"https://statsapi.web.nhl.com/api/v1/"

    def get_team_data(self):
        response = requests.get(f"{self.url}teams", verify=False, headers=HEADER)
        if response.status_code == 200:
            return response.json()
        else:
            return "ERROR: %s" % response.text


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
    nhl = WebScrape()
    team_df = create_dataframe(nhl.get_team_data(), "teams")
    print(team_df)


if __name__ == '__main__':
    main()
