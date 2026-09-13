import math


numberOfTeammates = input("Enter the number of teammates: ")
if numberOfTeammates.isdigit():
    numberOfTeammates = int(numberOfTeammates)
    if numberOfTeammates > 0:
        print(numberOfTeammates)
    else:
        print("invalid input")
else:
    print("invalid input")
rank = input("Enter your rank: ")
if rank.isdigit():
    rank = int(rank)
    if rank > 0:
        print(rank)
    else:
        print("invalid input")
else:
    print("invalid input")
numberOfTeams = input("Enter the number of teams: ")
if numberOfTeams.isdigit():
    numberOfTeams = int(numberOfTeams)
    if numberOfTeams > 0:
        print(numberOfTeams)
    else:
        print("invalid input")
else:
    print("invalid input")
for t in range(0, 361, 30):
    part1 = 100000/math.sqrt(numberOfTeammates)
    part2 = pow(rank, -0.75)
    part3 = math.log10(1 + math.log10(numberOfTeams))
    part4 = math.exp(-t/500)

    points = part1 * part2 * part3 * part4
    print(t, round(points, 2))
