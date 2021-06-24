#! /usr/bin/env python
import numpy as np

if __name__ == '__main__':

    freeSpace = np.zeros((10,10),dtype=np.int16)
    obstacleSpace = np.zeros((11,11), dtype=np.int16)
    freeSpace[0,1] = 1
    freeSpace[5,3] = 1
    freeSpace[8,8] = 1
    freeSpace[5,2] = 1
    freeSpace[5,4] = 1
    freeSpace[5,5] = 1

    xmoveStack = []
    ymoveStack = []
    pathCost = [0, 0]
    lastX = 0
    lastY = 0

    x, y = 1, 1
    rows = freeSpace.shape[0]
    cols = freeSpace.shape[1]

    for x in range(0, cols):
        for y in range(0, rows):
            obstacleSpace[x,y] = freeSpace[x,y]

    rows = obstacleSpace.shape[0]
    cols = obstacleSpace.shape[1]

    for x in range(1, 10):
        for y in range(1, 10):
            cells = [obstacleSpace[x-1,y-1], obstacleSpace[x-1,y+1], obstacleSpace[x+1,y-1], 
            obstacleSpace[x+1,y+1], obstacleSpace[x-1,y], obstacleSpace[x+1,y], 
            obstacleSpace[x,y+1], obstacleSpace[x,y-1]]

            smallest = 20
            present = False
            for i in cells:
                if i == 1:
                    present = True
                if i < smallest and i != 0:
                    smallest = i

            if present == True and obstacleSpace[x,y] != 1:
                obstacleSpace[x,y] = 2
            elif present == False and obstacleSpace[x,y] != 1:
                obstacleSpace[x,y] = smallest+1

    obsSpace = obstacleSpace

    x = 1
    y = 9

    xt = 6
    yt = 1

    obstacleSpace[xt,yt] = 0

    print(obstacleSpace)
    xpathSpace = obstacleSpace
    print(xpathSpace)
    while x != xt or y != yt:

        if lastX==xt and lastY==yt:
            print("stuck at:")
            print(xt)
            print(yt)
            break
        lastX=xt
        lastY=yt

        xpathSpace[xt,yt] = 0
        if x < xt and y < yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
                elif xcells[1] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[2] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x < xt and y > yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
                elif xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x > xt and y < yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
                elif xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x > xt and y > yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
                elif xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x == xt and y < yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
                elif xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x == xt and y > yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
                elif xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x < xt and y == yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
                elif xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
                elif xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
            else:
                print("x stuck")
                xmoveStack.clear()
        elif x > xt and y == yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[2] > 1:
                    xmoveStack.append(3)
                    xt = xt + 1
                elif xcells[3] > 1:
                    xmoveStack.append(0)
                    yt = yt - 1
                elif xcells[1] > 1:
                    xmoveStack.append(2)
                    yt = yt + 1
                elif xcells[0] > 1:
                    xmoveStack.append(1)
                    xt = xt - 1
            else:
                print("x stuck")
                xmoveStack.clear()
    print(xpathSpace)
    print(xmoveStack)