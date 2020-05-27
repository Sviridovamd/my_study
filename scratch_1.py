#with open( 'C:\\Users\\XPS\\Desktop\\dataset_3363_3.txt') as inf:
text = open("C:\\Users\\XPS\\Desktop\\dataset_3363_3.txt", 'r')
line0 = text.read().replace('\n', ' ').split()
#line = []
#text = open("C:\\Users\\XPS\\Desktop\\dataset_3363_3.txt", 'r')
#line = text.read().replace('\n', ' ').lower().split()
line = [i.lower() for i in line0]



#line = [str(i) for i in line0[i].upper()]
text.close()
print(line0, line)

linemax = 'a'
    # print(line_spi)
countmax = 0
for i in range (len(line)):
    if line.count(line[i]) > countmax:
        countmax = line.count(line[i])
        linemax = line0[i]
print(linemax, countmax )