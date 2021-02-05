import time
x = 0
def doIt(i):
    global x
    x = x + i
def doIt2(l):
    x = 0
    for i in l:
        x += i
    print(x)
def doIt3(l):
    x = 0
    list(map(lambda y: x = x + y ,l))
    print(x)
# def doIt1(list):
#     global x
#     for i in list:
#         x = x + i
# def doIt3(list):
#     global l
#     l = [i for i in list]
# def doIt4(i):
#     print(i)
    

s = []
l = range(10000000)
# t = time.time()
# for i in list:
#     doIt(i)
# print("%.3f" %(time.time() - t))

t = time.time()
doIt2(l)
print("%.3f" %(time.time() - t))

t = time.time()
doIt3(l)
print("%.3f" %(time.time() - t))

# t = time.time()
# doIt4(list)
# print("%.3f" %(time.time() - t))

# list(map(doIt4, [(1,2), (2,3)]))
# print(sum(list(map(lambda x: x[0] + x[1] ,[(1,2), (2,3)]))))
2000 * 50




