# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# solution("camelCasing")  ==  "camel Casing"
def solution(s):
    s = [str(i) for i in s]
    for i in range(len(s)):
        if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            s[i] = ' '+ s[i]
    return ''.join(s)

# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

# import re
# def solution(s):
#     return re.sub('([A-Z])', r' \1', s)