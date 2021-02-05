import math

fileNames = ["test.txt","a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
number = 6

with open(fileNames[number]) as file :
    list1 = file.read().splitlines()

fLine = list1[0]
total_books = int(fLine.split(" ")[0])
total_libraries = int(fLine.split(" ")[1])
total_days = int(fLine.split(" ")[2])

books_dict = []
books_score = []
is_book_scanned = []
for score in list1[1].split(" "):
    books_score.append(int(score))
    is_book_scanned.append(False)
   

lib_dict = []
libCount = 0
for i in range(2, total_libraries*2+2, 2):
    lib = {}
    lib["index"] = libCount
    lib["noOfBooks"] = int(list1[i].split(" ")[0])
    lib["daysNeedForSignUp"] = int(list1[i].split(" ")[1])
    lib["noOfBooksShipPerDay"] = int(list1[i].split(" ")[2])
    idList = list1[i+1].split(" ")
    lib["idsOfBooks"] = sorted(idList, key=lambda x: books_score[int(x)], reverse=True)
    lib["libScoreForCapacity"] = 0
    lib["scannedBooks"] =  [] 
    lib_dict.append(lib)
    libCount += 1

new_Lib_dict = []
new_Lib_dict.extend(lib_dict)

days = 0
lib_signUp = []
books_scanned = 0
score = 0

def setLib(lib):
    remaingDays = total_days - days - lib["daysNeedForSignUp"] 
    idsOfBooks = []
    idsOfBooks = list(filter(lambda bId: not is_book_scanned[int(bId)], lib_dict[lib["index"]]["idsOfBooks"]))
    lib_dict[lib["index"]]["idsOfBooks"] =  idsOfBooks
    idsOfBooks = idsOfBooks[:min( remaingDays * lib["noOfBooksShipPerDay"], len(idsOfBooks))]
       
    lib["idsOfBooks"] = idsOfBooks
    lib["noOfBooks"] = len(idsOfBooks) 
    if number == 4:
        lib["libScoreForCapacity"] = len(idsOfBooks)*65
    elif number == 2:
        lib["libScoreForCapacity"] = len(idsOfBooks)*100
    else:
        lib["libScoreForCapacity"] = sum(map(lambda bId: books_score[int(bId)], idsOfBooks ))

    #lib["capacity"] =  lib["libScoreForCapacity"] / lib["daysNeedForSignUp"] # 2ND = 5,822,900, 3RD = 5,689,822 and 4TH = 5,028,010
    #lib["capacity"] =  int(lib["libScoreForCapacity"] / 12000) / int(lib["daysNeedForSignUp"]/4) * lib["noOfBooks"]  # 6th = 5,345,656
    lib["capacity"] =  int(lib["libScoreForCapacity"] / 3000) / int(lib["daysNeedForSignUp"]/4) * lib["noOfBooks"]  # 6th = 5,345,656
    #lib["capacity"] =  (1+ int(lib["libScoreForCapacity"] / 9155)) / (1+int(lib["daysNeedForSignUp"]/1)) # 5th = 5,023,570
    # 5th = 5,034,898
    #lib["capacity"] =  (lib["libScoreForCapacity"] / lib["daysNeedForSignUp"]) * lib["noOfBooks"] # 6th = 5,331,760 # 2ND = 5,822,900 
    

    #Observation
    #2nd file  read_on =  only signUp days varies so it need to be ordered to minimum number of signup days.
    #it make highest possible score for 2nd = 5,822,900
    return lib
booksRemoved = []

while len(new_Lib_dict) > 0:
    new_Lib_dict = list(map(setLib, new_Lib_dict))
    new_Lib_dict.sort(key=lambda x: x["capacity"], reverse=True)
    if(new_Lib_dict[0]["noOfBooks"] == 0):
        new_Lib_dict.remove(new_Lib_dict[0])
        continue
    #print(sum(map(lambda lib: lib["libScoreForCapacity"], new_Lib_dict )) / len(new_Lib_dict))
    if days + new_Lib_dict[0]["daysNeedForSignUp"] > total_days :
        new_Lib_dict.remove(new_Lib_dict[0])
        continue
    days += new_Lib_dict[0]["daysNeedForSignUp"]
    lib_signUp.append(new_Lib_dict[0]["index"])

    #print(new_Lib_dict[0]["index"],new_Lib_dict[0]["noOfBooks"], new_Lib_dict[0]["daysNeedForSignUp"], new_Lib_dict[0]["noOfBooksShipPerDay"], new_Lib_dict[0]["libScoreForCapacity"], new_Lib_dict[0]["capacity"] )
    lib_dict[new_Lib_dict[0]["index"]]["scannedBooks"] = new_Lib_dict[0]["idsOfBooks"]
    books_scanned += new_Lib_dict[0]["noOfBooks"]
    score += new_Lib_dict[0]["libScoreForCapacity"]

    for id in new_Lib_dict[0]["idsOfBooks"]:
        is_book_scanned[int(id)] = True
    new_Lib_dict.remove(new_Lib_dict[0])
    #print(days)

print(fileNames[number])
print("Library Signed up on time : ", len(lib_signUp))
print("Books Scanned on time : ", books_scanned)
print("Score : ", score)

output = str(len(lib_signUp)) + "\n"
for libIndex in lib_signUp:
    output += str(lib_dict[libIndex]["index"]) + " "+ str(len(lib_dict[libIndex]["scannedBooks"])) + "\n"
    output += " ".join(lib_dict[libIndex]["scannedBooks"]) + "\n"

with open("out_" + fileNames[number], "w") as file1:
    file1.write(output)
