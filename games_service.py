import scores_data

def getNumberofGamesPlayed(seasonScores, team_name):
    games = 0
    for game_data_dict in seasonScores:
        if game_data_dict['team1'] == team_name:
            games += 1
        if game_data_dict['team2'] == team_name:
            games += 1
    return games
