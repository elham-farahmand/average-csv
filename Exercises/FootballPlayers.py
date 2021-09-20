# This program has two classes. Human is the parent class and Footbalist is the child class.
# We give a list of 22 names of football players to the program and it spreads players into two teams randomly.
# At the end it prints each player's name and team.

import random

class Human:
    def __init__ (self, name):
        self.name = name
    def get_name(self):
        return self.name

class Footbalist(Human):
    def team_football (self, team):
        self.team = team
    def get_team(self):
        return self.team

names = 'حسین - مازیار - اکبر - نیما -  مهدی - فرهاد - محمد - خشایار - میلاد - مصطفی - امین - سعید - پویا - پوریا - رضا - علی - بهزاد - سهیل - بهروز - شهروز - سامان - محسن'
names_list = names.split(' - ')
players = list()
final = list()

for i in range(22):
    players.append(Footbalist (names_list[i]))

for i in range(11):
    rand = random.randint(0,22-i)
    players[rand].team_football('A')
    final.append(players[rand])
    players.remove(players[rand])

for person in players:
    person.team_football('B')
    final.append(person)

for item in final:
    print(item.get_name(), item.get_team())


