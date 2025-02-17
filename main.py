import numpy
import csv

games = []
with open("games2022.csv", "r") as file:
    for row in file:
        games.append(row.strip().split(","))
print(games)

D1 = set()
for row in games:
    if row[21] == 'TRUE':
        D1.add(row[0])
print(D1)

i = 0
while i < len(games):
    if games[i][0] in D1:
        games.pop(i)
        i -= 1
    i += 1

print(games)
with open("output.csv", "w", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerows(games)
