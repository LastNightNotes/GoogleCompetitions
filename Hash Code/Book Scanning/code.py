import math

fileNames = ["test.txt","a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
number = 5

file = open(fileNames[number])
list1 = file.read().splitlines()
file.close()

fLine = list1[0]
total_books = int(fLine.split(" ")[0])
total_libraries = int(fLine.split(" ")[1])
total_days = int(fLine.split(" ")[2])

count = 0
books_dict = []
for score in list1[1].split(" "):
    book = {}
    book["index"] = count
    book["score"] = int(score)
    book["scanned"] = False
    books_dict.append(book)
    count += 1


lib_dict = []
i = 2
libCount = 0
while i < total_libraries*2+2:
    lib = {}
    lib["libScoreForCapacity"] = 0  
    lib["index"] = libCount
    lib["noOfBooks"] = int(list1[i].split(" ")[0])
    lib["daysNeedForSignUp"] = int(list1[i].split(" ")[1])
    lib["noOfBooksShipPerDay"] = int(list1[i].split(" ")[2].replace("\n", ""))
    idList = list1[i+1].split(" ")
    lib["idsOfBooks"] = sorted(idList, key=lambda x: books_dict[int(x)]["score"], reverse=True)
    lib["scannedBooks"] =  [] 
    lib_dict.append(lib)
    i += 2
    libCount += 1

days = 0
maxScore = 0
removedBookIdsList = []
#print(lib_dict)
def setLib(lib):       
    newListOfBookIds = []
    lib["libScoreForCapacity"] = 0
    day3 = days + lib["daysNeedForSignUp"]
    for bookId in lib["idsOfBooks"]:
        if books_dict[int(bookId)]["scanned"] == False:
            countDays = day3 + math.ceil((len(newListOfBookIds) + 1) / lib["noOfBooksShipPerDay"])
            if countDays <= total_days:
                newListOfBookIds.append(bookId)
                if number == 4:
                    lib["libScoreForCapacity"] += 65
                else:
                    lib["libScoreForCapacity"] += books_dict[int(bookId)]["score"]

    lib["idsOfBooks"] = newListOfBookIds
    lib["noOfBooks"] = len(newListOfBookIds)
    lib["capacity"] =  (lib["noOfBooks"] / lib["daysNeedForSignUp"]) # 2nd = 5,822,900, 3rd = 5,689,822 # 6th = 5,308,034 # 5th = 4,987,661  4th = 5,028,010
    return lib


print("Total books : " + str(total_books))

new_lib_dict = []
#new_lib_dict.extend(lib_dict)

#print(lib_dict)
score = 0
books_scanned = 0
lib_signUp = []
# while days <= total_days and len(new_lib_dict) > 0:
#     new_lib_dict = list(map(setLib, new_lib_dict ))
#     new_lib_dict.sort(key=lambda x: x["capacity"], reverse=True) 
#     if new_lib_dict[0]["noOfBooks"] == 0:
#         new_lib_dict.remove(new_lib_dict[0])
#         continue
#     if days + new_lib_dict[0]["daysNeedForSignUp"] < total_days:
#         lib_signUp.append(new_lib_dict[0]["index"])
#         days += new_lib_dict[0]["daysNeedForSignUp"]
#         dVal = days
#         j = 0
#         z = new_lib_dict[0]["noOfBooksShipPerDay"]
#         lib_dict[new_lib_dict[0]["index"]]["scannedBooks"].extend(new_lib_dict[0]["idsOfBooks"])
#         score += new_lib_dict[0]["libScoreForCapacity"]
#         books_scanned.extend(new_lib_dict[0]["noOfBooks"])
#         for id in new_lib_dict[0]["idsOfBooks"]:
#             books_dict[int(id)]["scanned"] = True
#         new_lib_dict.remove(new_lib_dict[0])

#ar = [204, 694, 210, 719, 595, 618, 774, 901, 422, 369, 312, 672, 622, 828, 209, 563, 454]
ar = [602, 522 ]
# 204 31 6 389728
# 694 35 6 366387
# 719 41 8 377542
# 210 30 8 332672
# 901 45 9 368223
# 774 45 5 365726
# 422 48 7 369703
# 672 51 9 369821
# 618 40 10 316089
# 622 49 7 355007
# 595 37 6 293887
# 147 51 5 343640
# 312 40 7 287111
# 369 37 7 267940
# 563 44 10 273749
# 454 32 8 188299
# 431 30 8 66236

empyArray = []
for id in ar:
    empyArray.append(lib_dict[id])
new_lib_dict = empyArray
while len(new_lib_dict) > 0:
    new_lib_dict = list(map(setLib, new_lib_dict ))
    #new_lib_dict.sort(key=lambda x: x["capacity"], reverse=True) 
    if new_lib_dict[0]["noOfBooks"] == 0:
        new_lib_dict.remove(new_lib_dict[0])
        continue
    if days + new_lib_dict[0]["daysNeedForSignUp"] < total_days:
        lib_signUp.append(new_lib_dict[0]["index"])
        days += new_lib_dict[0]["daysNeedForSignUp"]
        dVal = days
        j = 0
        z = new_lib_dict[0]["noOfBooksShipPerDay"]
        lib_dict[new_lib_dict[0]["index"]]["scannedBooks"].extend(new_lib_dict[0]["idsOfBooks"])
        score += new_lib_dict[0]["libScoreForCapacity"]
        books_scanned += new_lib_dict[0]["noOfBooks"]
        for id in new_lib_dict[0]["idsOfBooks"]:
            books_dict[int(id)]["scanned"] = True
        new_lib_dict.remove(new_lib_dict[0])

print(fileNames[number])
print("Books Scanned on time : " + str(books_scanned))
print("Score : " + str(score))

output = str(len(lib_signUp)) + "\n"
for libIndex in lib_signUp:
    print(lib_dict[libIndex]["index"], lib_dict[libIndex]["daysNeedForSignUp"], len(lib_dict[libIndex]["scannedBooks"]), lib_dict[libIndex]["libScoreForCapacity"] )
    output += str(lib_dict[libIndex]["index"]) + " "+ str(len(lib_dict[libIndex]["scannedBooks"])) + "\n"
    output += " ".join(lib_dict[libIndex]["scannedBooks"]) + "\n"

file1 = open("out_" + fileNames[number], "w")
file1.write(output)
file1.close()