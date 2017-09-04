# port2.py

import csv

total = 0.0

with open('../data/portfolio2.csv', 'r') as f:
	rows = csv.reader(f)
	headers = next(f) # Skip a single line of input
	for row in rows:
		row[2] = int(row[2])
		row[3] = float(row[3])
		total += row[2] * row[3]

print('Total cost:', total)


