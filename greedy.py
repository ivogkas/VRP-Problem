import random
import math

class Node:
    def __init__(self, id, tp, dem, xx, yy):
        self.id = id
        self.type = tp
        self.demand = dem
        self.x = xx
        self.y = yy
all_nodes = []
service_locations = []
depot = Node(0, 0, 0, 50, 50)
all_nodes.append(depot)
random.seed(1)

for i in range(0, 200):
    id = i + 1
    tp = random.randint(1,3)
    dem = random.randint(1,5) * 100
    xx = random.randint(0, 100)
    yy = random.randint(0, 100)
    serv_node = Node(id, tp, dem, xx, yy)
    all_nodes.append(serv_node)
    service_locations.append(serv_node)




dist_matrix = [[0.0 for j in range(0, len(all_nodes))] for k in range(0, len(all_nodes))]
for i in range(0, len(all_nodes)):
    for j in range(0, len(all_nodes)):
        source = all_nodes[i]
        target = all_nodes[j]
        dx_2 = (source.x - target.x)**2
        dy_2 = (source.y - target.y) ** 2
        dist = round(math.sqrt(dx_2 + dy_2))
        dist_matrix[i][j] = dist


hour_matrix = [[0.0 for j in range(0, len(all_nodes))] for k in range(0, len(all_nodes))]
for i in range(0, len(all_nodes)):
    for j in range(0, len(all_nodes)):
        time = dist_matrix[i][j] / 35
        hour_matrix[i][j] = time



vehicles_road = []
for i in range(0,25):
    vehicles_road.append([0])



visit_node = [[0.0 for j in range(0, 200)] for k in range(0, 25)]
for i in range(0,25):
    for j in range(0,200):
        visit_node[i][j] = 0


vehicles_supplies = {}
for i in range(0,25):
    vehicles_supplies[i] = [3000, 0]


def findVechileMinTime(times):
    min = 1000 * 1000
    veh = -1
    for i in times:
        if times[i][1] <= min and times[i][0] >= 400:
            min = times[i][1]
            veh = i
    return veh


class move():
    min_time = 100 * 100
    travel_time = None
    total_time = None


def node_service(mv):
    vehicle_with_min_time = findVechileMinTime(vehicles_supplies)
    free = vehicles_supplies[vehicle_with_min_time][0]
    for i in (service_locations):
        if (i.type == 1):
            unload_time = 1 / 12
        elif (i.type == 2):
            unload_time = 3 / 12
        else:
            unload_time = 5 / 12
        destination = vehicles_road[vehicle_with_min_time][len(vehicles_road[vehicle_with_min_time]) - 1]
        mv.travel_time = hour_matrix[destination] [i.id]
        mv.total_time = mv.travel_time + unload_time

        if mv.total_time < mv.min_time and free >= i.demand:
            mv.min_time = mv.total_time
            node_visit = i

    service_locations.remove(node_visit)
    vehicles_supplies[vehicle_with_min_time][0] = vehicles_supplies[vehicle_with_min_time][0] - node_visit.demand
    vehicles_road[vehicle_with_min_time].append(node_visit.id)
    vehicles_supplies[vehicle_with_min_time][1] = vehicles_supplies[vehicle_with_min_time][1] + mv.min_time



for i in range (0,200):
    mv = move()
    node_service(mv)

for i in vehicles_road:
    i.append(0)












