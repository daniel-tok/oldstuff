def make_bricks(small, big, goal):
    smallLength = 1
    bigLength = 5
    max = (bigLength * big) +(smallLength * small)
    remBig = goal % bigLength
    if max < goal:
        return False
    else:
        if remBig < 5 and