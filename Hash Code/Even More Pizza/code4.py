import operator
import math
import numpy as np
import pandas as pd

from functools import reduce
files = ['a_example','a_test.txt', 'b_little_bit_of_everything.in', 'c_many_ingredients.in', 'd_many_pizzas.in', 'e_many_teams.in']
# files = files[4:]
# files = files[:1]
# A – Example 74 points
# B – A little bit of everything 8,598 points
# C – Many ingredients 612,757,485 points
# D – Many pizzas 5,637,787 points
# E – Many teams 8,331,852 points
# 626,735,796

# a = RR
# b = RN
# C = NR
# D = NR
# e = code1.py
for file in files:
    with open(file) as f:
        firstLine = f.readline()
        totalPizza, noOf2PersonTeam, noOf3PersonTeam, noOf4PersonTeam = list(map(int,firstLine.split()))
        teams = [2]*noOf2PersonTeam + [3]*noOf3PersonTeam + [4]*noOf4PersonTeam
        pizzas = []
        uniqueIng = []
        maxIng = 0
        minIng = 0
        for i in range(totalPizza):
            y = f.readline().split()
            x = y[1:]
            
            pizzas.append({"oIndex": i, "ing":x, "ingCount": int(y[0])})
            uniqueIng += x
        if file != 'e_many_teams.in':  
            pizzas.sort(key=lambda x: x["ingCount"], reverse=True)
            maxIng = pizzas[0]["ingCount"]
        else: 
            pizzas.sort(key=lambda x: x["ingCount"])
            maxIng = pizzas[-1]["ingCount"]

        possibleDeliveries = []
        if file == 'e_many_teams.in': teams = list(reversed(teams))
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
        # print("Unique Ingredients", len(set(uniqueIng)), firstLine)
        if file not in  ["b_little_bit_of_everything.in",'e_many_teams.in' ]: 
            possibleDelivery = list(reversed(possibleDelivery))
        # print(possibleDelivery)
        ans = "" + str(len(possibleDelivery)) + "\n"
        i = 0
        j = len(pizzas) - 1
        score = 0
        for team in possibleDelivery:
            l = []
            ans += str(team) + " "
            s = 0
            if file == "b_little_bit_of_everything.in":
                param1 = 1 
            # else: param1 = 500
            else: param1 = 100
            while s < maxIng-(s//param1) and team:
                ans += str(pizzas[i]["oIndex"]) + " "
                l += pizzas[i]["ing"]
                i+= 1
                team -= 1
                s = len(set(l))
                # print(file, s, maxIng, score)
            for z in range(team):
                ans += str(pizzas[j]["oIndex"]) + " "
                l += pizzas[j]["ing"]
                j-= 1
               
            score += len(set(l))**2
            ans += "\n"
        print("Score:",file ,": ",score)
        # print(ans)
        # data.to_html(file+".html")
        # print(data)
        with open("output_" + file, "w") as f2:
            f2.write(ans)
        


