import scores_data

def getUniqueTeamsData(seasonScores):
    uniqueTeams = set()
    for score in seasonScores:
        uniqueTeams.add(score['team1'])
        uniqueTeams.add(score['team2'])
    return uniqueTeams
