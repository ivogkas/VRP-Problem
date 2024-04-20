from greedy import *


class end():
    flag = True


end = end()


def findDemand(point):
    for node in all_nodes:
        if node.id == point:
            return node.demand

def findUnloadTime(point):
    for nd in all_nodes:
        if nd.id  == point:
            if (nd.type == 1):
                return 1 / 12
            elif (nd.type == 2):
                return 3 / 12
            else:
                return 5 / 12



def try_relocation(originRouteIndex, targetRouteIndex, originRtCostChange, targetRtCostChange):
    max = 0
    for i in vehicles_supplies:
        if i == originRouteIndex:
            if vehicles_supplies[i][1] + originRtCostChange > max:
                max = vehicles_supplies[i][1] + originRtCostChange
        if i == targetRouteIndex:
            if vehicles_supplies[i][1] + targetRtCostChange > max:
                max = vehicles_supplies[i][1] + targetRtCostChange
        if vehicles_supplies[i][1] > max and originRouteIndex != i and targetRouteIndex != i:
            max = vehicles_supplies[i][1]
    return max


class RelocationMove():
    originRoutePosition = None
    targetRoutePosition = None
    originNodePosition = None
    targetNodePosition = None
    costChangeOriginRt = None
    costChangeTargetRt = None
    minMaxTime = 10000*1000


def StoreBestRelocationMove(originRouteIndex, targetRouteIndex, originNodeIndex, targetNodeIndex, moveCost, originRtCostChange, targetRtCostChange, rm:RelocationMove):
    rm.originRoutePosition = originRouteIndex
    rm.originNodePosition = originNodeIndex
    rm.targetRoutePosition = targetRouteIndex
    rm.targetNodePosition = targetNodeIndex
    rm.costChangeOriginRt = originRtCostChange
    rm.costChangeTargetRt = targetRtCostChange
    rm.moveCost = moveCost



def CalculateMinMax(time):
    c = 0
    for i in (time):
        if time[i][1] > c :
            c = time[i][1]
    return c



def FindBestRelocationMove(rm: RelocationMove):
    for originRouteIndex in range(0, len(vehicles_road)):
        rt1 = vehicles_road[originRouteIndex]
        for targetRouteIndex in range (0, len(vehicles_road)):
            rt2 = vehicles_road[targetRouteIndex]
            for originNodeIndex in range (1, len(rt1) - 1):
                for targetNodeIndex in range (0, len(rt2) - 1):

                    if originRouteIndex == targetRouteIndex and (targetNodeIndex == originNodeIndex or targetNodeIndex == originNodeIndex - 1):
                        continue


                    A = rt1[originNodeIndex - 1]
                    B = rt1[originNodeIndex]
                    C = rt1[originNodeIndex + 1]

                    F = rt2[targetNodeIndex]
                    G = rt2[targetNodeIndex + 1]

                    if rt1 != rt2:
                        if vehicles_supplies[targetRouteIndex][0] -  findDemand(B) < 0:
                            continue

                    # if Node B is the last node of route1, not care about cost A to depot
                    if originNodeIndex == len(rt1) - 2:
                        originRtCostChange = - hour_matrix[A][B]
                    else:
                        originRtCostChange = hour_matrix[A][C] - hour_matrix[A][B] - hour_matrix[B][C]
                    # if node F is the last node of route2, not care about cost B to depot
                    if targetNodeIndex == len(rt2) - 2:
                        targetRtCostChange = hour_matrix[F][B]
                    else:
                        targetRtCostChange = hour_matrix[F][B] + hour_matrix[B][G] - hour_matrix[F][G]

                    if rt1 != rt2:
                        originRtCostChange = originRtCostChange - findUnloadTime(B)
                        targetRtCostChange = targetRtCostChange + findUnloadTime(B)

                    minMaxTime = try_relocation(originRouteIndex, targetRouteIndex, originRtCostChange, targetRtCostChange)

                    if (minMaxTime <= rm.minMaxTime and vehicles_supplies[originRouteIndex][1] == CalculateMinMax(vehicles_supplies)):

                        rm.originRoutePosition = originRouteIndex
                        rm.targetRoutePosition = targetRouteIndex
                        rm.originNodePosition = originNodeIndex
                        rm.targetNodePosition = targetNodeIndex
                        rm.costChangeOriginRt = originRtCostChange
                        rm.costChangeTargetRt = targetRtCostChange
                        rm.minMaxTime = minMaxTime



def ApplyRelocationMove(rm: RelocationMove):

    oldMinMax = CalculateMinMax(vehicles_supplies)
    newMinMax = rm.minMaxTime

    if (oldMinMax < newMinMax ):
        end.flag = False

    else:
        originRt = rm.originRoutePosition
        targetRt = rm.targetRoutePosition

        B = vehicles_road[rm.originRoutePosition][rm.originNodePosition]

        if originRt == targetRt:
            del vehicles_road[originRt][rm.originNodePosition]
            if (rm.originNodePosition < rm.targetNodePosition):
                vehicles_road[targetRt].insert(rm.targetNodePosition, B)
            else:
                vehicles_road[targetRt].insert(rm.targetNodePosition + 1, B)

        else:
            del vehicles_road[originRt][rm.originNodePosition]
            vehicles_road[targetRt].insert(rm.targetNodePosition + 1, B)
            vehicles_supplies[originRt][1] += rm.costChangeOriginRt
            vehicles_supplies[targetRt][1] += rm.costChangeTargetRt
            vehicles_supplies[originRt][0] += findDemand(B)
            vehicles_supplies[targetRt][0] -= findDemand(B)



while end.flag == True:
    rm = RelocationMove()
    FindBestRelocationMove(rm)
    ApplyRelocationMove(rm)


for r in vehicles_road:
    r.pop()

print(CalculateMinMax(vehicles_supplies))
for i in vehicles_road:
    print(i)


