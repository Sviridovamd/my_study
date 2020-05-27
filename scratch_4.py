
s1 = [str(i) for i in input()]
s2 = [str(i) for i in input()]
A = dict (zip (s1,s2))
D = dict (zip (s2,s1))
answer = [str(i) for i in input()]
qwestion = [str(i) for i in input()]

for i in answer:
    if i in A:
        print(A[i],end='')
print()
for j in qwestion:
    if j in D:
        print(D[j], end='')