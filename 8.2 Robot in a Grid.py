def getPath(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    if isPath(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def isPath(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    isAtOrigin = (row == 0) and (col == 0)

    if isAtOrigin or isPath(maze, row, col-1) or isPath(maze, row-1, col, path):
        point = (row, col)
        path.append(point)
        return True

    return False
