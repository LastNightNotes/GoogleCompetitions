import os
files = ['a_example', 'b_little_bit_of_everything.in', 'c_many_ingredients.in', 'd_many_pizzas.in', 'e_many_teams.in']
files = files[4:]
# A – Example 61 points
# B – A little bit of everything 7,480 points
# C – Many ingredients 204,889,772 points
# D – Many pizzas 1,462,883 points
# E – Many teams 4,451,557 points
# 210,811,753
for file in files:
    with open(file) as f:
        firstLine = f.readline()
        totalPizza, noOf2PersonTeam, noOf3PersonTeam, noOf4PersonTeam = list(map(int,firstLine.split()))
        teams = [2]*noOf2PersonTeam + [3]*noOf3PersonTeam + [4]*noOf4PersonTeam
        pizzas = []
        for i in range(totalPizza):
            pizzas.append(f.readline().split()[1:])
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
        ans = "" + str(len(possibleDelivery)) + "\n"
        i = 0
        j = 0
        for team in possibleDelivery:
            ans += str(team) + " "
            j += team
            while i < j:
                ans += str(i) + " "
                i+= 1
            ans += "\n"
        
        with open("output_" + file, "w") as f2:
            f2.write(ans)


# file1 = open("output.txt", "w")
# file1.write(str(numberOfSlidesinSS) + "\n")

# for item in slideshow:
#     file1.write(str(item["index"]) + "\n")
# file1.close()


