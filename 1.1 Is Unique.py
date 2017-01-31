# My Solution
def isUnique(str):
    d = dict()
    for i in str:
        if d.get(i,0) == 0:
            d[i] = 1
        else:
            d[i] += 1
    for _, j in d.items():
        if j != 1:
            return False
    return True

print(isUnique("asdf!!"))

# Another Solution
import unittest

def isUnique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('asdf'),('')]
    dataF = [('abcda'), ('assdf'), ('asf3fasf3=34')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()



