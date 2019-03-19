import scores_data

def getTotalPointsScores(seasonScores, team_name):
    pointsScored = 0
    for game_data_dict in seasonScores:
        if game_data_dict['team1'] == team_name:
            pointsScored += int(game_data_dict['score1'])
        if game_data_dict['team2'] == team_name:
            pointsScored += int(game_data_dict['score2'])
#web: gunicorn weightTrackerProject.wsgi
    return pointsScored


def getTotalPointsGivenUp(seasonScores, team_name):
    pointsGivenUp = 0
    for game_data_dict in seasonScores:
        if game_data_dict['team1'] == team_name:
            pointsGivenUp += int(game_data_dict['score2'])
        if game_data_dict['team2'] == team_name:
            pointsGivenUp += int(game_data_dict['score1'])
    return pointsGivenUp
