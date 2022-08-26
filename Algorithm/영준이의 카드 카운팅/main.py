import sys
sys.stdin = open("sample_input.txt", "r")


t = int(input())
for tc in range(1, 1+t):
    S = input()
    card = [[] for _ in range(4)]       # S, D, H, C

    for i in range(0, len(S), 3):
        if S[i] == 'S':
            if S[i+1:i+3] in card[0]:
                ans = ' ERROR'
                break
            card[0].append(S[i+1:i+3])
        elif S[i] == 'D':
            if S[i+1:i+3] in card[1]:
                ans = ' ERROR'
                break
            card[1].append(S[i+1:i+3])
        elif S[i] == 'H':
            if S[i+1:i+3] in card[2]:
                ans = ' ERROR'
                break
            card[2].append(S[i+1:i+3])
        elif S[i] == 'C':
            if S[i+1:i+3] in card[3]:
                ans = ' ERROR'
                break
            card[3].append(S[i+1:i+3])
    else:
        ans = ''
        for c in card:
            ans += ' ' + str(13-len(c))

    print(f'#{tc}{ans}')
