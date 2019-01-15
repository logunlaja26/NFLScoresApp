from flask import Flask, jsonify, redirect, url_for, render_template
import csv
import scores_data
import teams_service

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

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
	for score in scores_data.get2017scores():
		getScore = Score(score['date'],score['team1'],score['team2'],score['score1'],score['score2'])
		scores.append(getScore.__dict__)
	return jsonify(scores)


class Team:
	def __init__(self,firstScore,secondScore):
		self.firstScore = firstScore
		self.secondScore= secondScore




@app.route("/api/teams")
def teams():
	teams = teams_service.getatlantaData()
	#return jsonify(teams)
	data = []
	for team in teams:
		teamData = Team(team['score1'],team['score2'])
		data.append(teamData.__dict__)
	return jsonify(data)





if __name__ == "__main__":
	app.run(debug=True)
