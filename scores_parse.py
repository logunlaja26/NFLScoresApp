import csv

# with open('nfl_games.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)


	# for line in csv_reader:
	# 	print(line)

with open('nfl_games.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for line in csv_reader:
		print(line)
