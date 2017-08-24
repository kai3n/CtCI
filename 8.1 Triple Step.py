def tripleStep(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)

print(tripleStep(2))

def Method2(x):
    memo = [-1] * (x + 1)
    return TripleHopRecursive(x, memo)


def TripleHopRecursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]