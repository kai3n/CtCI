import unittest

def checkPermutation(strSet):
    str1 = strSet[0]
    str2 = strSet[1]
    if len(str1) != len(str2):
        return False
    d = dict()
    for i in str1:
        if d.get(i,0) == 0:
            d[i] = 1
        else:
            d[i] += 1
    for i in str2:
        if d.get(i,0) == 0:
            return False
        d[i] -= 1
    return True

class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = checkPermutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = checkPermutation(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()


