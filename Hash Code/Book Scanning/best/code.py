import math
fileNames = ["test.txt","a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
number = 6
file = open(fileNames[number])
list1 = file.readlines()
file.close()
fLine = list1[0]
total_books = fLine.split(" ")[0]
total_libraries = int(fLine.split(" ")[1])
total_days = int(fLine.split(" ")[2])
#print(total_books,  total_libraries,total_days)

books_dict = []
for score in list1[1].split(" "):
    book = {}
    book["score"] = int(score.replace("\n", ""))
    book["scanned"] = []
    book["inLib"] = []
    books_dict.append(book)
    

#print(books_dict)

lib_dict = []
i = 2
while i < total_libraries*2+2:
    lib = {}
    lib["noOfBooks"] = list1[i].split(" ")[0]
    lib["daysNeedForSignUp"] = int(list1[i].split(" ")[1])
    lib["noOfBooksShipPerDay"] = int(list1[i].split(" ")[2].replace("\n", ""))
    lib["idsOfBooks"] = list1[i+1].replace("\n", "").split(" ")
    lib["scannedBooks"] = []
    lib_dict.append(lib)
    i += 2

#print(lib_dict)
fb = []
def getFinalList(libIndex):
    booksList = lib_dict[libIndex]["idsOfBooks"]
    # finalBookList = []
    # for bookIndex in booksList:
    #     if len(books_dict[int(bookIndex)]["scanned"]) < 1:
    #         finalBookList.append(bookIndex)
    # print(finalBookList, booksList)
    return booksList

def scanBook(libIndex, dayValue):
    dVal = dayValue
    j = 0
    z = lib_dict[libIndex]["noOfBooksShipPerDay"]
    while  j < len(fb):
        if(dVal > total_days): 
            pass
        dVal += 1
        scanned = {}
        scanned["on"] = libIndex
        scanned["day"] = dVal
     
        for t in range(z):
            try:
                books_dict[int(fb[j+t])]["scanned"].append(scanned)
                lib_dict[libIndex]["scannedBooks"].append(fb[j+t])
            except IndexError:
                pass
        j += z   

for book in books_dict:
    book["index"] = books_dict.index(book)

for lib in lib_dict:
    lib["index"] = lib_dict.index(lib)
    lib["capacity"] =  len(lib["idsOfBooks"]) / (lib["daysNeedForSignUp"] + 
    math.ceil(len(lib["idsOfBooks"]) / lib["noOfBooksShipPerDay"]))
    lib["idsOfBooks"].sort(key=lambda x: books_dict[int(x)]["score"])


# for book in books_dict:
#     for lib in lib_dict:
#         if str(book["index"]) in lib["idsOfBooks"]:
#             book["inLib"].append(lib["index"])


sortedLib_dict = sorted(lib_dict, key=lambda x: x["capacity"], reverse=True)
emptyArray = []
for lib in sortedLib_dict:
    newListOfBookIds = []
    for bookId in lib["idsOfBooks"]:
        if bookId not in emptyArray:
            emptyArray.append(bookId)
            newListOfBookIds.append(bookId)
    lib["idsOfBooks"] = newListOfBookIds

for lib in sortedLib_dict:
    lib["capacity"] =  len(lib["idsOfBooks"]) / (lib["daysNeedForSignUp"] + 
    math.ceil(len(lib["idsOfBooks"]) / lib["noOfBooksShipPerDay"]))


sortedLib_dict = sorted(sortedLib_dict, key=lambda x: x["capacity"], reverse=True)
print(len(emptyArray))
print("Books in Libraries after final Sorting : " + str(len(emptyArray)))
print("Total books : " + str(total_books))


#print(sortedLib_dict)
day = 0
lib_signUp = []
for lib in sortedLib_dict:
    if day + lib["daysNeedForSignUp"] < total_days:
        fb =  getFinalList(lib["index"])
        #print(fb)
        if len(fb) > 0:
            lib_signUp.append(lib["index"])
            day += lib["daysNeedForSignUp"]
            scanBook(lib["index"], day)

#print(lib_dict)
#print(books_dict)


books_scanned = []

for l in range(int(total_books)):
    try:
        if books_dict[l]["scanned"][0]["day"] <= total_days:
                books_scanned.append(l)
    except IndexError:
        pass

score = 0
for bookIndex in books_scanned:
    score += books_dict[bookIndex]["score"]
    #print(bookIndex)
print("Books Scanned : " + str(len(books_scanned)))
print("Score : " + str(score))

maxScore = 0
for book in books_dict:
    maxScore += book["score"]
print("Max Score : " + str(maxScore))



output = str(len(lib_signUp)) + "\n"
for libIndex in lib_signUp:
    output += str(lib_dict[libIndex]["index"]) + " "+ str(len(lib_dict[libIndex]["scannedBooks"])) + "\n"
    output += " ".join(lib_dict[libIndex]["scannedBooks"]) + "\n"

file1 = open("out_" + fileNames[number], "w")
file1.write(output)
file1.close()
