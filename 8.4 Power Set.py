def powerSet(s):
    x = len(s)
    for i in range(1 << x):
        print([s[j] for j in range(x) if i & (1 << j)])

powerSet(['a', 'b', 'c', 'd'])