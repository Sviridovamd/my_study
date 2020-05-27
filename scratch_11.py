# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
#
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
def maskify(cc):
    cc = [str(i) for i in cc]
    print (cc)
    for i in range(len(cc)-4):
        cc[i] = '#'
    cc = ''.join([str(j) for j in cc])
    return cc

cc = 'SF$SDfgsd2eA'
r = maskify(cc)
print("masking: {0}".format(cc))
print("{0}  matches  {1}".format(cc,r))
print(r, cc)

# cc = '123'
# r = maskify(cc)
# test.describe("masking: {0}".format(cc))
# test.it("{0}  matches  {1}".format(cc, r))
# test.assert_equals(r, cc)
#
# cc = 'SF$SDfgsd2eA'
# r = maskify(cc)
# test.describe("masking: {0}".format(cc))
# test.it("{0}  matches  {1}".format('########d2eA', r))
# test.assert_equals(r, '########d2eA')