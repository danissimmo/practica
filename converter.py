import csv
import itertools

with open('log.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    stripped = [line.replace(","," ").split() for line in lines]
    grouped = zip(*[stripped]*1)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow((' Source ', ' Target ', ' distance '))
        for group in grouped:
            writer.writerows(group)