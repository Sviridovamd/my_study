n = int(input())
A = {}
for i in range(n):
    a = input().lower()
    A[a] = 0
n1 = int(input())
for i in range(n1):
    st = [str(s) for s in input().split()]
    for j in range(len(st)):
        if st[j].lower() not in A:
            A[st[j].lower()] = 0
            print(st[j])

