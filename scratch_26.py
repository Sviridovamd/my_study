# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
def unique_in_order(iterable):
    iterable = [x for x in iterable ]
    for i in range(1,len(iterable)-1):
        if iterable[len(iterable)-i-1] == iterable[len(iterable)-i]:
            iterable.pop(len(iterable)-i-1)
    if len(iterable)>1 and iterable[0] == iterable[1]:
        iterable.pop(0)
    return iterable

print(unique_in_order('AAAABBBCCDAABBB'))#, ['A','B','C','D','A','B'])
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1,2,2,3,3]))