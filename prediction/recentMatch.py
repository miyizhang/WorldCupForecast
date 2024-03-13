import pandas as pd

# Load the CSV file
matches_df = pd.read_csv('data/results.csv')
matches_df = matches_df.iloc[:-48]

matches_df["date"] = pd.to_datetime(matches_df["date"])


def get_recent_matches(home_team, away_team, number_of_matches=5):
    filtered_matches = matches_df[((matches_df['home_team'] == home_team) & (matches_df['away_team'] == away_team)) |
                                  ((matches_df['home_team'] == away_team) & (matches_df['away_team'] == home_team))]

    sorted_matches = filtered_matches.sort_values(by='date', ascending=False)

    recent_matches = sorted_matches.head(number_of_matches)

    recent_matches_list = recent_matches.to_dict(orient='records')
    return recent_matches_list
