
file = open("input.txt")
list1 = file.readlines()
file.close()
total_photos = list1[0]
#print(list1, total_photos)
data = []


for i in range(1,int(total_photos)+1):
    dict1 = {}
    dict1["type"] = list1[i].replace("\n", "").split(" ")[0]
    dict1["tagsCount"] = int(list1[i].replace("\n", "").split(" ")[1])
    dict1["tags"] = list1[i].replace("\n", "").split(" ")[2:]
    data.append(dict1)
    
slideshow = []
listOfVPics = []
for item in data:
    if item["type"] == "H":
        item["index"] = data.index(item)
        slideshow.append(item)
    else:
        listOfVPics.append(data.index(item))


if len(listOfVPics) >= 2:
    if len(listOfVPics) % 2 != 0:
        listOfVPics.pop()
    i = 0
    while(i < len(listOfVPics) ):
        item = {}
        item["type"] = 'V'
        item["index"] = str(listOfVPics[i]) +" " + str(listOfVPics[i+1])
        tags = data[listOfVPics[i]]["tags"]
        for tag in data[listOfVPics[i+1]]["tags"]:
            if tag not in data[listOfVPics[i]]["tags"]:
                tags.append(tag)
        item["tags"] = tags
        item["tagsCount"] = len(tags)
        slideshow.append(item)
        i += 2

numberOfSlidesinSS = len(slideshow)
file1 = open("output.txt", "w")
file1.write(str(numberOfSlidesinSS) + "\n")

for item in slideshow:
    file1.write(str(item["index"]) + "\n")
file1.close()

for item in slideshow:
    print(item)

score = 0
for i in range(len(slideshow) - 1):
    commonTags = 0
    for tag in slideshow[i]["tags"]:
        if tag in slideshow[i+1]["tags"]:
            commonTags += 1
    
    difInFirst = slideshow[i]["tagsCount"] - commonTags
    difInSecond = slideshow[i+1]["tagsCount"] - commonTags
    score += min(commonTags, difInFirst, difInSecond)

print(score)
