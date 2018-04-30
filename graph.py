import copy

class connections:
    def __init__(self, target_node, distance):
        self.target_node = target_node
        self.distance = distance


class node:
    def __init__(self, lable=0):
        self.lable = lable
        self.connections = []
        self.traveled = 0
        self.visited = False
        self.occupied=[]
        self.path=[]

    # def __cmp__(self, other):
    #     return cmp(self.traveled,other.traveled)

    def draw(self):
        print(self.lable, end='    ->   ')
        for i in range(len(self.connections)):
            print(self.connections[i].target_node.lable, '(', self.connections[i].distance, ')', end=', ')
        print('')


class graph:
    def __init__(self):
        self.nodes = []

    def reset(self):
        for i in range(len(self.nodes)):
            self.nodes[i].traveled = 0
            self.nodes[i].visited = False
            self.nodes[i].path=[]

    def add_node(self, lable=0):
        self.nodes.append(node(lable))

    def get_node(self, lable):
        for i in range(len(self.nodes)):
            if self.nodes[i].lable == lable:
                return self.nodes[i]

    def make_connection(self, node1: node, node2: node, distance):
        flag = True
        for i in range(len(node1.connections)):
            if node2 == node1.connections[i].target_node:
                flag = False
        if node1 != node2 and flag:
            node1.connections.append(connections(node2, distance))
            node2.connections.append(connections(node1, distance))

    # def make_connections(self, current_node: node, node_list: list):
    #     for i in range(len(node_list)):
    #         self.make_connection(current_node, node_list[i])

    def draw(self):
        for i in range(len(self.nodes)):
            self.nodes[i].draw()

    def dijkstra(self,start_node :node, finish_node:node):
        priority_que = [start_node]
        start_node.visited = True
        while True:
            priority_que.sort(key=getKey)
            current = priority_que[0]
            if current is finish_node:
                current.path.append(current.lable)
                for i in range(len(current.path)):
                    self.get_node(current.path[i]).occupied.append(self.get_node(current.path[i]).traveled)
                path=current.path
                self.reset()
                return path
            priority_que.pop(0)
            for i in range(len(current.connections)):
                if (current.traveled + current.connections[i].distance) not in current.connections[i].target_node.occupied:
                    if not current.connections[i].target_node.visited:
                        current.connections[i].target_node.traveled = current.traveled + current.connections[i].distance
                        priority_que.append(current.connections[i].target_node)
                        current.connections[i].target_node.path=copy.deepcopy(current.path)
                        current.connections[i].target_node.path.append(current.lable)
                        current.connections[i].target_node.visited = True
                    else:
                        if current.traveled + current.connections[i].distance < current.connections[i].target_node.traveled:
                            current.connections[i].target_node.traveled = current.traveled + current.connections[i].distance
                            current.connections[i].target_node.path=copy.deepcopy(current.path)
                            current.connections[i].target_node.path.append(current.lable)
def getKey(node:node):
        return node.traveled

g = graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(5)
g.add_node(4)
g.make_connection(g.get_node(1), g.get_node(2), 10)
g.make_connection(g.get_node(2), g.get_node(4), 8)
g.make_connection(g.get_node(1), g.get_node(3), 4)
g.make_connection(g.get_node(3), g.get_node(4), 4)
g.make_connection(g.get_node(1), g.get_node(5), 5)
g.make_connection(g.get_node(5), g.get_node(4), 6)
m=g.dijkstra(g.get_node(1), g.get_node(4))
for i in range(len(m)):
    print(m[i],'  ',g.get_node(m[i]).occupied)
m=g.dijkstra(g.get_node(2), g.get_node(3))
for i in range(len(m)):
    print(m[i],'  ',g.get_node(m[i]).occupied)