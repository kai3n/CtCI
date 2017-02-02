import unittest

def palindromePermutation(str):
    d = dict()
    for i in str.replace(" ","").lower():
        if d.get(i, 0) == 0:
            d[i] = 1
        else:
            d[i] += 1
    cnt = 0
    for k, v in d.items():
        if v & 1 == 1:
            cnt += 1
    if cnt > 1:
        return False
    else:
        return True

print(palindromePermutation("Tact Coa"))
