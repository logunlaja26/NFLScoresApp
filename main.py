from flask import Flask, jsonify
import csv

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def csvParser():
	output = []
	with open('nfl_games.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for line in csv_reader:
		 	output.append(line)
	return jsonify({'nfl_scores': output})


if __name__ == "__main__":
	app.run(debug=True)
	
	