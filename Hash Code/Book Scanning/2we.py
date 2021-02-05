import math

fileNames = ["test.txt","a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
number = 5

file = open(fileNames[number])
list1 = file.readlines()
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
    book["score"] = int(score.replace("\n", ""))
    book["scanned"] = []
    books_dict.append(book)
    count += 1

#print(books_dict)

lib_dict = []
i = 2
libCount = 0
while i < total_libraries*2+2:
    lib = {}
    lib["index"] = libCount
    lib["noOfBooks"] = int(list1[i].split(" ")[0])
    lib["daysNeedForSignUp"] = int(list1[i].split(" ")[1])
    lib["noOfBooksShipPerDay"] = int(list1[i].split(" ")[2].replace("\n", ""))
    idList = list1[i+1].replace("\n", "").split(" ")
    lib["idsOfBooks"] = sorted(idList, key=lambda x: books_dict[int(x)]["score"], reverse=True)
    lib["libScoreForCapacity"] = 0
    lib["scannedBooks"] =  [] 
    lib_dict.append(lib)
    i += 2
    libCount += 1


new_Lib_dict = []
new_Lib_dict.extend(lib_dict)

days = total_days
lib_signUp = []
while days > 0 and len(new_Lib_dict) > 0:
     
    for lib in new_Lib_dict:
        remaingDays = days
        remaingDays -= lib["daysNeedForSignUp"]
        TBIT =  remaingDays * lib["noOfBooksShipPerDay"]
        idsOfBooks = []
        lib["libScoreForCapacity"] = 0
        books_done = 0
        possible_score = 0
        for bId in lib["idsOfBooks"]:
          if len(books_dict[int(bId)]["scanned"]) == 0:
              lib["libScoreForCapacity"] += books_dict[int(bId)]["score"]
              idsOfBooks.append(int(bId))
              books_done += 1
              if TBIT == books_done:
                  possible_score = lib["libScoreForCapacity"]
        if TBIT < len(idsOfBooks):
            idsOfBooks = idsOfBooks[:TBIT]
            lib["libScoreForCapacity"] = possible_score
        
        lib["idsOfBooks"] = idsOfBooks
        lib["noOfBooks"] = len(idsOfBooks) 
        
            
        lib["capacity"] =  (lib["libScoreForCapacity"] / lib["daysNeedForSignUp"] ) # 2ND = 5,822,900, 3RD = 5,689,822 and 4TH = 5,028,010 
        #lib["capacity"] =  lib["noOfBooks"] / lib["daysNeedForSignUp"]  # 6TH = 5,317,660 and 2ND = 5,822,900
        #lib["capacity"] =  (lib["noOfBooks"] / lib["daysNeedForSignUp"] ) * lib["noOfBooksShipPerDay"]  # 5TH = 4,894,015 and 2ND = 5,822,900 and 4TH = 5,028,010

        #Observation
        #lib["capacity"] =  1 / lib["daysNeedForSignUp"] # in 2nd file read_on only signUp days varies so it need to be ordered to minimum number of signup days.
        # it make highest possible score for 2nd = 5,822,900


    new_Lib_dict.sort(key=lambda x: x["capacity"], reverse=True)
    if(new_Lib_dict[0]["noOfBooks"] == 0):
        pass
    days -= new_Lib_dict[0]["daysNeedForSignUp"]
    if days > 0 :
        lib_signUp.append(new_Lib_dict[0]["index"])
        rmDays = days
        total_books_in_time = rmDays * new_Lib_dict[0]["noOfBooksShipPerDay"]
        total_books_to_do = new_Lib_dict[0]["noOfBooks"]
        ids_list = new_Lib_dict[0]["idsOfBooks"]
    
        if total_books_in_time < total_books_to_do:
            print("Less books are done!")
            for i in range(total_books_in_time):
                books_dict[int(ids_list[i])]["scanned"].append(new_Lib_dict[0]["index"])
                lib_dict[new_Lib_dict[0]["index"]]["scannedBooks"].append(str(ids_list[i]))
            newDemoTotalBooksInTime = total_books_in_time
            while newDemoTotalBooksInTime < total_books_to_do:
                print(books_dict[ids_list[newDemoTotalBooksInTime]]["index"],new_Lib_dict[0]["index"] ) 
                newDemoTotalBooksInTime += 1
        else:
            for bID in ids_list:
                books_dict[int(bID)]["scanned"].append(new_Lib_dict[0]["index"])
                lib_dict[new_Lib_dict[0]["index"]]["scannedBooks"].append(str(bID))

        new_Lib_dict.remove(new_Lib_dict[0])



books_scanned = []
print(lib_signUp)
for l in range(total_books):
    try:
        if len(books_dict[l]["scanned"]) == 1:
            books_scanned.append(l)
    except IndexError:
        pass

score = 0

for bookIndex in books_scanned:
    score += books_dict[bookIndex]["score"]

print("Books Scanned on time : " + str(len(books_scanned)))
print("Score : " + str(score))


output = str(len(lib_signUp)) + "\n"
for libIndex in lib_signUp:
    output += str(lib_dict[libIndex]["index"]) + " "+ str(len(lib_dict[libIndex]["scannedBooks"])) + "\n"
    output += " ".join(lib_dict[libIndex]["scannedBooks"]) + "\n"

file1 = open("out_" + fileNames[number], "w")
file1.write(output)
file1.close()
    
    


