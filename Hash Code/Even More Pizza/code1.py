import operator
import math
import numpy as np
import pandas as pd

from functools import reduce
files = ['a_example', 'b_little_bit_of_everything.in', 'c_many_ingredients.in', 'd_many_pizzas.in', 'e_many_teams.in']
# files = files[4:]
files = files[1:2]
# A – Example 74 points
# B – A little bit of everything 7,505 points
# C – Many ingredients 204,889,772 points
# D – Many pizzas 1,466,599 points
# E – Many teams 5,069,205 points
# 211,433,155
for file in files:
    with open(file) as f:
        firstLine = f.readline()
        totalPizza, noOf2PersonTeam, noOf3PersonTeam, noOf4PersonTeam = list(map(int,firstLine.split()))
        teams = [2]*noOf2PersonTeam + [3]*noOf3PersonTeam + [4]*noOf4PersonTeam
        pizzas = []
        uniqueIng = []
        for i in range(totalPizza):
            x = f.readline().split()[1:]
            
            pizzas.append({"oIndex": i, "ing":x})
            uniqueIng += x
        if file in  ['a_example', "e_many_teams.in"]: 
            pizzas.sort(key=lambda x: len(x["ing"]))

        data = pd.DataFrame(pizzas)
        
        possibleDeliveries = []
        
        for i,team in enumerate(teams):
            p = totalPizza
            l = []
            j = i
            while j < len(teams) and p - teams[j] >= 0:
                l.append(teams[j])
                p -= teams[j]
                j += 1
            if l not in possibleDeliveries: possibleDeliveries.append(l)
            break
        possibleDelivery = possibleDeliveries[0]
        print("Unique Ingredients", len(set(uniqueIng)))
        if file != "c_many_ingredients.in": possibleDelivery = list(reversed(possibleDelivery))
        print(possibleDelivery)
        ans = "" + str(len(possibleDelivery)) + "\n"
        i = 0
        j = 0
        score = 0
        for team in possibleDelivery:
            l = []
            ans += str(team) + " "
            j += team
            while i < j:
                ans += str(pizzas[i]["oIndex"]) + " "
                l += pizzas[i]["ing"]
                i+= 1
            score += len(set(l))**2
            ans += "\n"
        print("Score:",file ,": ",score)
        # print(ans)
        data.to_html(file+".html")
        # print(data)
        with open("output_" + file, "w") as f2:
            f2.write(ans)
        


