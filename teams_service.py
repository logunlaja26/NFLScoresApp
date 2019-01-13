import scores_data

def getatlantaData():
    scores = []
    for score in scores_data.get2017scores():
        if score['team1'] == 'ATL' or score['team2'] == 'ATL':
            scores.append(score)
    return scores
