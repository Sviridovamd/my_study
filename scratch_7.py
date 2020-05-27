text = open("C:\\Users\\XPS\\Desktop\\dataset_3380_5.txt", 'r')
line0 = text.read().split()
A = {}
sumrost = 0

for i in range(0,len(line0),3):
    if int(line0[i]) not in A:
        A[int(line0[i])] = [int(line0[i+2])]
    else:
        A[int(line0[i])] += [int(line0[i + 2])]
for key in range(1,12):
    if key not in A:
        print(key,'-')
    else:
        x = A.get(key)
        sumrost = 0
        srrost = 0
        for i in x:

            sumrost += i
        srrost = sumrost/(len(x))
        print(key,srrost )
