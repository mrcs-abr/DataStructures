import sys

n_players = int(input())

players = input().split()

if len(players) != n_players:
    sys.exit()
    
players = [int(i) for i in players]
players = sorted(players, reverse=True)

first_team = players[:11]
bench_players = players[11:]

if len(bench_players) > 11:
    bench_players = players[11: 22]

t = 0
r = 0

for i in first_team:
    t += i

for i in bench_players:
    r += i

print(t - r)









