from flask import Flask, jsonify, redirect, url_for
import csv

app = Flask(__name__)


@app.route("/")
def index():
	indexFileUrl = url_for('static', filename='index.html')
	return redirect(indexFileUrl)

@app.route("/<staticFileName>")
def staticFile(staticFileName):
	staticFileUrl = url_for('static', filename=staticFileName)
	return redirect(staticFileUrl)

class Score:
	def __init__(self,dateOfContest,homeTeam,awayTeam,homeTeamScores,awayTeamScores):
		self.dateOfContest = dateOfContest
		self.homeTeam = homeTeam
		self.awayTeam = awayTeam
		self.homeTeamScores = homeTeamScores
		self.awayTeamScores = awayTeamScores


@app.route("/api/scores")
def csvParser():
	scores = []
	with open('nfl_games.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for score in csv_reader:
			if score['season'] == '2017':
				gameScore = Score(score['date'],score['team1'],score['team2'],score['score1'],score['score2'])
				scores.append(gameScore.__dict__)
	return jsonify(scores)

@app.route("/api/historicalPage")
def historicalPage():
	return "Testing..."

if __name__ == "__main__":
	app.run(debug=True)
