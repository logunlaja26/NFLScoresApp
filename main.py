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

@app.route("/api/scores")
def csvParser():
	output = []
	with open('nfl_games.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for line in csv_reader:
		 	output.append(line)
	return jsonify({'nfl_scores': output})


if __name__ == "__main__":
	app.run(debug=True)
	
	