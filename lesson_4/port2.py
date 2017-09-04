import csv
import glob


def portfolio_cost(filename):
	'''
	Computes total shares * price for a CSV file
	with structure: name, data, shres, price
	'''

	total = 0.0

	with open(filename, 'r') as f:
		rows = csv.reader(f)
		headers = next(f) # Skip a single line of input
		for row in rows:
			row[2] = int(row[2])
			row[3] = float(row[3])
			total += row[2] * row[3]

	return total

)


if __name__ == "__main__":
	filename = ('../data/portfolio.csv')
	total = portfolio_cost(filename)
	print('Total cost:', total)
else:
	print('name not main!')
