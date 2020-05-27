#Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
def iq_test(numbers):
    numbers1 = [str(s) for s in numbers.split()]
    i = 0


    test = [x for x in numbers.split() if not int(x) % 2]
    test2 = [x for x in numbers.split() if int(x) % 2]
    if len(test)>len(test2):
        while numbers1[i] != test2[0]:
                i += 1
    else:
        while numbers1[i] != test[0]:
            i += 1


    return i+1