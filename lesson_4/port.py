# port.py

import csv


def portfolio_cost(filename, *, errors='warn'):

	'''
	Computers total shares * price for a CSV file
	with name, date, shares, price data
	'''
	if errors not in {'warn', 'silent', 'raise'}:
    		raise ValueError("errors must be one of 'warn', 'silent', or 'raise'")
	total = 0.0
	with open(filename, 'r') as f:
		rows = csv.reader(f) # Read in rows of csv file
		headers = next(rows) # Skip header row
		for row_num, row in enumerate(rows, start=1):
			try: # If it's possible program fails
				row[2] = int(row[2])
				row[3] = float(row[3])
			
			# except Exception as err: # Not really best practice
			except ValueError as err:
				if errors == 'warn':
					print('Row:', row_num, 'Bad row:', row)
					print('Row:', row_num, 'Reason:', err)
				elif errors == 'raise':
					raise # Reraises last exception
				else:
					pass # Ignore
				continue # Skips to the next row
			total += row[2] * row[3]
	return total

total = portfolio_cost('../data/missing.csv', errors='silent')
print('Total cost:', total)
