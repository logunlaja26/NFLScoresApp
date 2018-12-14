from flask import Flask
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
	return output


if __name__ == "__main__":
	app.run(debug=True)
	
	