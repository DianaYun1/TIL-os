import sys

sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, 1 + t):
    S = input()
    card = [[] for _ in range(4)]  # S, D, H, C
    name = ['S', 'D', 'H', 'C']

    for i in range(0, len(S), 3):
        for j in range(4):
            if S[i] == name[j]:
                if S[i + 1:i + 3] in card[j]:
                    ans = 'ERROR'
                    print(f'#{tc} {ans}')
                    break

                else:
                    card[j].append(S[i + 1:i + 3])
    else:
        ans = []
        for c in card:
            ans.append(13 - len(c))
        print(f'#{tc}', *ans)
