from flask import Flask, jsonify, redirect, url_for, render_template
import csv
import scores_data
import teams_service
import games_service
import game_scores

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<staticFileName>")
def staticFile(staticFileName):
	staticFiles = ['runtime.js','polyfills.js','styles.js','vendor.js','main.js']
	if staticFileName in staticFiles:
		staticFileUrl = url_for('static', filename=staticFileName)
		return redirect(staticFileUrl)

	return render_template('index.html')

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
	def __init__(self,teamName,averagePointsScored,averagePointsgivenup):
		self.teamName = teamName
		self.averagePointsScored = averagePointsScored
		self.averagePointsgivenup= averagePointsgivenup




@app.route("/api/teams")
def getTeamsData():
	teamsData = []
	teams = teams_service.getUniqueTeamsData(scores_data.seasonScores)
	for team_name in teams:
		games = games_service.getNumberofGamesPlayed(scores_data.seasonScores, team_name)
		totalPoints = game_scores.getTotalPointsScores(scores_data.seasonScores, team_name)
		totalGivenUp = game_scores.getTotalPointsGivenUp(scores_data.seasonScores, team_name)
		avgPointsScored = totalPoints / games
		avgPointsGivenUp = totalGivenUp / games
		teamData = Team(team_name, round(avgPointsScored), round(avgPointsGivenUp))
		teamsData.append(teamData.__dict__)
	return jsonify(teamsData)

if __name__ == "__main__":
	app.run(debug=True)
