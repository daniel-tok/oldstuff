# V1 - doesn't return False when impossible but returns True

def make_bricks(small, big, goal):
    smallBricks = 1
    bigBricks = 5
    noOfSmall = 0
    noOfBig = 0
    while noOfSmall <= small:
        test = (noOfBig * bigBricks) + (noOfSmall * smallBricks)
        if test == goal:
            return True
        elif noOfBig <= big:
            noOfBig += 1
        elif noOfBig > big:
            noOfBig = 0
            noOfSmall += 1
        elif noOfSmall > small:
            return False

print(make_bricks(1, 1, 8))


