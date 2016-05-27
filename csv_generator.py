#!/usr/bin/env python

import csv, argparse, random, string

parser = argparse.ArgumentParser(description='Generate a CSV of random data.')
parser.add_argument('rows', help='Number of rows of data to generate')
parser.add_argument('columns', help='Number of columns of data to generate')
parser.add_argument('filename', help='Where to write the generated data')

args = parser.parse_args()

DATUM_LENGTH = 6

headers = []
for col in range(0, int(args.columns)):
    headers.append('Header-' + col)

output = csv.writer(open(args.filename, 'wb'))
output.writerow(headers)

for row in range(0, int(args.rows)):
    data = []
    for col in range(0, int(args.columns)):
        data.append(''.join(random.choice(string.ascii_lowercase) for _ in range(DATUM_LENGTH)))
    output.writerow(data)
