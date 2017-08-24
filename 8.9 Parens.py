def generateParens(remaining):
    hashSet = set()
    if remaining == 0:
        hashSet.add('')
    else:
        prev = generateParens(remaining-1)
        for str in prev:
            for i in range(len(str)):
                if str[i] == '(':
                    s = insertInside(str, i)
                    hashSet.add(s)
            hashSet.add('()' + str)

    return hashSet

def insertInside(str, leftIndex):
    left = str[:leftIndex+1]
    right = str[leftIndex+1:]
    return left + '()' + right

print(generateParens(3))