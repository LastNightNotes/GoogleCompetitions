import operator
import math
import numpy as np
import pandas as pd

from functools import reduce
files = ['a_example', 'b_little_bit_of_everything.in',
         'c_many_ingredients.in', 'd_many_pizzas.in', 'e_many_teams.in']
# files = files[4:]
files = files[:1]
# A – Example 74 points
# B – A little bit of everything 8,598 points
# C – Many ingredients 612,757,485 points
# D – Many pizzas 5,637,787 points
# E – Many teams 6,266,626 points
# 624,670,570

# a = RR
# b = RN
# C = NR
# D = NR
# e = code1.py
for file in files:
    with open(file) as f:
        firstLine = f.readline()
        totalPizza, noOf2PersonTeam, noOf3PersonTeam, noOf4PersonTeam = list(
            map(int, firstLine.split()))
        teams = [2]*noOf2PersonTeam + [3]*noOf3PersonTeam + [4]*noOf4PersonTeam
        pizzas = []
        uniqueIng = []
        maxIng = 0
        minIng = 0
        for i in range(totalPizza):
            y = f.readline().split()
            x = y[1:]

            pizzas.append({"oIndex": i, "ing": x, "ingCount": int(y[0])})
            uniqueIng += x

        pizzas.sort(key=lambda x: x["ingCount"], reverse=True)
        maxIng = pizzas[0]["ingCount"]
        uniqueIng = set(uniqueIng)
        print(uniqueIng) 
        print(pd.DataFrame(pizzas) ) 

        d = {}
        for pizza in pizzas:
            n = pizza["ingCount"]
            d[n] = d.get(n, [])
            d[n].append(pizza["oIndex"])

        e = {}
        for pizza in pizzas:
            for ing in pizza["ing"]:
                e[ing] = e.get(ing, [])
                e[ing].append(pizza["oIndex"])
        e = dict(sorted(e.items(), key=lambda x: len(x[1])))
        print(d,e)
        
       
        deliveries = []
        
        while totalPizza:
            minPizzaRequiredForMaxScore = math.ceil(len(e)/maxIng)
            delivery = {"team": minPizzaRequiredForMaxScore}
            pizzasInThisDelivery = []
            ingredientsList = []
            totalPizza -= minPizzaRequiredForMaxScore
            
            while minPizzaRequiredForMaxScore:
                print("i", i)
                compPizzas = []
                keysToDel = []
                for ing in e:
                    if len(e[ing]) == 1 and ing not in ingredientsList:
                        compPizzas += e[ing]
                        keysToDel.append(ing)
            
                compPizzas = list(set(compPizzas))
                print("compPizzas", compPizzas)
                if compPizzas:
                    pizzasInThisDelivery += compPizzas
                    
                    for p in compPizzas:
                        for ing in e:
                            if p in e[ing]:
                                e[ing].remove(p)
                                ingredientsList.append(ing) 
                else:
                    f = {}
                    for ing in e:
                        if ing not in ingredientsList:
                            print(ing)
                            for p in e[ing]:
                                f[p] = f.get(p, 0) + 1
                    f = sorted(f.items(), key=lambda x: x[1], reverse=True)
                    # print(e,f,pizzasInThisDelivery)
                    pizzasInThisDelivery += [f[0][0]]
                    for ing in e:
                        if f[0][0] in e[ing]:
                            e[ing].remove(f[0][0])
                            ingredientsList.append(ing)
                            if len(e[ing]) == 0: keysToDel.append(ing)
                print(e,keysToDel)
                minPizzaRequiredForMaxScore -= len(pizzasInThisDelivery)
                for key in keysToDel:
                    e.pop(key) 
            delivery["pizzas"] =  pizzasInThisDelivery
            deliveries.append(delivery)
        print(deliveries,e,ingredientsList)



        # for l in d:
        #     u= uniqueIng.copy()
        #     u = u - set(pizzas[d[l][-1]]["ing"])
        #     d[l].pop()
        #     if len(u) > maxIng: requiredIng = maxIng

        #     u = u - set(pizzas[d[requiredIng][-1]]["ing"])
        #     d[requiredIng].pop()

        #     if len(u) > maxIng: requiredIng = maxIng
        #     else: requiredIng = maxIng

        #     u = u - set(pizzas[d[requiredIng][-1]]["ing"])
        #     d[requiredIng].pop()
        #     print(d,u)
                

        # possibleDeliveries = []
        # if file == 'e_many_teams.in': teams = list(reversed(teams))
        # for i,team in enumerate(teams):
        #     p = totalPizza
        #     l = []
        #     j = i
        #     while j < len(teams) and p - teams[j] >= 0:
        #         l.append(teams[j])
        #         p -= teams[j]
        #         j += 1
        #     if l not in possibleDeliveries: possibleDeliveries.append(l)
        #     break
        # possibleDelivery = possibleDeliveries[0]
        # print("Unique Ingredients", len(set(uniqueIng)), firstLine)
        # if file not in  ["b_little_bit_of_everything.in",'e_many_teams.in' ]:
        #     possibleDelivery = list(reversed(possibleDelivery))
        # # print(possibleDelivery)
        # ans = "" + str(len(possibleDelivery)) + "\n"
        # i = 0
        # j = len(pizzas) - 1
        # score = 0
        # for team in possibleDelivery:
        #     l = []
        #     ans += str(team) + " "
        #     s = 0
        #     if file == "b_little_bit_of_everything.in":
        #         param1 = 1
        #     else: param1 = 500
        #     while s < maxIng-(s//param1) and team:
        #         ans += str(pizzas[i]["oIndex"]) + " "
        #         l += pizzas[i]["ing"]
        #         i+= 1
        #         team -= 1
        #         s = len(set(l))
        #         # print(file, s, maxIng, score)
        #     for z in range(team):
        #         ans += str(pizzas[j]["oIndex"]) + " "
        #         l += pizzas[j]["ing"]
        #         j-= 1

        #     score += len(set(l))**2
        #     ans += "\n"
        # print("Score:",file ,": ",score)
        # # print(ans)
        # # data.to_html(file+".html")
        # # print(data)
        # with open("output_" + file, "w") as f2:
        #     f2.write(ans)
