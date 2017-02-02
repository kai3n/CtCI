def stringCompression(s):
    s += " "
    r = ""
    i = 0
    while i < len(s)-1:
        beg = i
        while s[i] == s[i+1]:
            i += 1
        end = i
        r += s[beg] + str(end-beg+1)
        i += 1
    return r

s = "aabccccaaaaa"
print(stringCompression(s))