import csv

def get2017scores():
    scores = []
    with open('nfl_games.csv', 'r') as csv_file:
    	csv_reader = csv.DictReader(csv_file)
    	for score in csv_reader:
    		if score['season'] == '2017':
    			scores.append(score)
    return scores
