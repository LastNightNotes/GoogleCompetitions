for tc in range(int(input())):
    number = input()
    B = ''.join('1' if d == '4' else '0' for d in number).lstrip('0')
    # A = int(number) - int(B)     # one way
    A = number.replace('4', '3') # 2nd way
    print('Case #{}: {} {}'.format(tc+1, A, B))