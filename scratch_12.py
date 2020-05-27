# A square of squares
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!
#
# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
#
# Task
# Given an integral number, determine if it's a square number:
#
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
#
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
from math import*

def is_square(n):
    import math
    if n < 0:
        a = "%s: Negative numbers cannot be square numbers" %n
        return False

    nsqrt = sqrt(n)
    if (nsqrt - int(nsqrt)) == 0:
        a = ("%s is a square number" %n)
        return True
    else:
        a = ("%s is not a square number" %n)
        return False # fix me