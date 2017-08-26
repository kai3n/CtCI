from collections import deque


def routeBetweenN(start, end):
    stack = deque()
    visited = set()

    stack.append(start)
    visited.add(start)

    while stack:
        node = stack.pop()
        if node == end:
            return True
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False
