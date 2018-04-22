class connections:
    def __init__(self, target_node, distance):
        self.target_node = target_node
        self.distance = distance

class node:
    def __init__(self, lable=0):
        self.lable = lable
        self.connections = []

    def draw(self):
        print(self.lable, end='    ->   ')
        for i in range(len(self.connections)):
            print(self.connections[i].target_node.lable, '(', self.connections[i].distance, ')', end=', ')
        print('')


class graph:
    def __init__(self):
        self.nodes = []

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
            node1.connections.append(connections(node2,distance))
            node2.connections.append(connections(node1,distance))

    # def make_connections(self, current_node: node, node_list: list):
    #     for i in range(len(node_list)):
    #         self.make_connection(current_node, node_list[i])

    def draw(self):
        for i in range(len(self.nodes)):
            self.nodes[i].draw()

    # def dijkstra(self,fir_node :node, sec_node:node):



g = graph()
g.add_node(4)
g.add_node(55)
g.add_node(12)
g.add_node(78)
g.make_connection(g.get_node(4), g.get_node(12), 3)
g.make_connection(g.get_node(55), g.get_node(12), 5)
g.make_connection(g.get_node(78), g.get_node(12), 4)
g.draw()


