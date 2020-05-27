with open( 'C:\\Users\\XPS\\Desktop\\dataset_3363_2.txt') as inf:
    line1 = []
    for line in inf:
        line = line.strip()
        i = 0
        l = len(line)
        num_out_of_line = []
        str_num = ""
        str_out_line = []
        line_out = []


        for i in range(len(line)):
            if line[i] in "0123456789":
                str_num += line[i]
                try:
                    if line[i + 1] not in "0123456789":
                        num_out_of_line.append(str_num)
                        str_num = ""
                except:
                    num_out_of_line.append(str_num)
        num_out_of_line = [int(i) for i in num_out_of_line]
        for i in range(len(line)):
            if line[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                str_out_line.append(line[i])
        for i in range(len(str_out_line)):
            line_out += [str_out_line[i]] * num_out_of_line[i]



        #print(list(map(int, num_out_of_line)))
        #print(str_out_line)
        print(' '.join([str(i) for i in line_out]))