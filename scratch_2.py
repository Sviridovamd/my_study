text = open("C:\\Users\\XPS\\Desktop\\dataset_3363_4.txt", 'r')
line0 = text.read().replace('\n', ' ').split()
a={}
b=[0,0,0]
for i in line0:
    i = [str(s) for s in i.split(';')]

    a[i[0]] = [(int(i[1])+int(i[2])+int(i[3]))/3]
    b[0] += int(i[1])
    b[1] += int(i[2])
    b[2] += int(i[3])

for j in range(len(b)):
    b[j] = b[j]/len(line0)




for key,value in a.items():
    print('\n'.join([str(i) for i in value]))



print(' '.join([str(i) for i in b]))
