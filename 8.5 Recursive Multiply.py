def multiply(a, b, answer):
    if b == 0:
        return answer
    else:
        answer += a
        return multiply(a, b-1, answer)

print(multiply(3, 6, 0))