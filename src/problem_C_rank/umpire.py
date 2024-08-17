N = int(input())

ball_count = 0
strike_count = 0

for _ in range(N):
    s = input()

    if s == 'ball':
        if ball_count == 3:
            print('fourball!')
            ball_count = 0
        else:
            print('ball!')
            ball_count += 1
    elif s == 'strike':
        if strike_count == 2:
            print('out!')
            strike_count = 0
        else:
            print('strike!')
            strike_count += 1
