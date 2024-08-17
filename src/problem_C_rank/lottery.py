b = int(input())
n = int(input())

for _ in range(n):
    a = int(input())
    
    # 1st Prize
    if a == b:
        print('first')
    # Adjacent Prize
    elif a == b - 1 or a == b + 1:
        print('adjacent')
    # 2nd Prize
    elif a % 10000 == b % 10000:
        print('second')
    # 3rd Prize
    elif a % 1000 == b % 1000:
        print('third')
    # Others
    else:
        print('blank')
