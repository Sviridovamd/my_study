a = [0,0]
n = int(input())
for i in range(n):
    s = [str(j) for j in input().split()]
    if s[0] == 'север':
        a[1] += int(s[1])
    elif s[0] == 'юг':
        a[1] -= int(s[1])
    elif s[0] == 'восток':
        a[0] += int(s[1])
    elif s[0] == 'запад':
        a[0] -= int(s[1])
print(' '.join([str(f) for f in a]))