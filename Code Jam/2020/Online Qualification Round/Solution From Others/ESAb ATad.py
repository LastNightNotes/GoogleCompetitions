import random
import copy
def BitFlip(s):
    return ''.join(str(1 - int(c)) for c in s)


def RandomBitString(b):
    return ''.join(str(random.randint(0, 1)) for _ in range(b))


def Reverse(s):
    return s[::-1]

def random_modify(test_case,j):
  if random.randint(1,2) == 1:
    test_case = BitFlip(test_case)
  if random.randint(1,2) == 1:
    test_case = Reverse(test_case)
  return test_case
t, b = [int(x) for x in input().split()]
n = b
def test():

    now = 1
    answer = '0' * b
    diff = -1
    same = -1
    answersame = '0'
    answerdiff = '0'

    while True:
        limit = 10
        if same != -1:
            print(same)
            limit -= 1
            inputsame = input()
            if answersame != inputsame:
                answer = BitFlip(answer)
                answerdiff = BitFlip(answerdiff)
                answersame = BitFlip(answersame)
        if diff != -1:
            print(diff)
            limit -= 1
            inputdiff = input()
            if answerdiff != inputdiff:
                answer = Reverse(answer)
                answerdiff = BitFlip(answerdiff)


        if limit % 2 == 1:
            print(1)
            x = input()
            limit-=1
        while limit > 0:
            print(now)
            one = input()

            print(n - now + 1)
            two = input()
            answer = answer[:now - 1] + one + answer[now:]
            answer = answer[:n - now] + two + answer[n - now+1:]
            if one == two:
                same = now
                answersame = one
            else:
                diff = now
                answerdiff = one
            limit -= 2
            now += 1
            if now > b/2:
              print(answer)
              input()
              return

for i in range(t):
    test()

