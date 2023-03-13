from exceptions import NodeNotInGraphError, NodeAlreadyInGraphError, VerticeAlreadyPresent, VerticeNotInGraph, ReflexiveVerticeNotAllowed

class Graph():
    def __init__(self, oriented=True):
        self.oriented = oriented
        self.nodes = dict()

    def add_node(self, node):
        if node in self.nodes:
            raise NodeAlreadyInGraphError(node)
        self.nodes[node] = set()

    def delete_node(self, node):
        if not self.lookup(node):
            raise NodeNotInGraphError(node)

        for node_b in self.nodes:
            if node in self.nodes[node_b]:
                self.nodes[node_b].remove(node)
        
        del self.nodes[node]


    def lookup(self, node):
        if node in self.nodes:
            return True
        return False

    def add_edge(self, node_a, node_b):
        if not self.lookup(node_a):
            raise NodeNotInGraphError(node_a)
        if not self.lookup(node_b):
            raise NodeNotInGraphError(node_b)
        if node_b in self.nodes[node_a]:
            raise VerticeAlreadyPresent(node_a, node_b)
        if node_a == node_b:
            ReflexiveVerticeNotAllowed(node_a, node_b)
        
        if not self.oriented:
            if node_a in self.nodes[node_b]:
                raise VerticeAlreadyPresent(node_b, node_a)
            
            self.nodes[node_b].add(node_a)

        self.nodes[node_a].add(node_b)

    def delete_edge(self, node_a, node_b):
        if not self.lookup(node_a):
            raise NodeNotInGraphError(node_a)
        if not self.lookup(node_b):
            raise NodeNotInGraphError(node_b)

        if node_b not in self.nodes[node_a]:
            raise VerticeNotInGraph(node_a, node_b)
        
        self.nodes[node_a].remove(node_b)

        if not self.oriented:
            if node_a not in self.nodes[node_b]:
                raise VerticeNotInGraph(node_b, node_a)
            self.nodes[node_b].remove(node_a)


    def enum_nodes(self):
        print(self.nodes.keys())


    def enum_edges(self):
        for node in self.nodes:
            for to_node in self.nodes[node]:
                print(f"Edge from {node} to {to_node}")


    def calculate_number_of_nodes(self):
        return len(self.nodes)

    def calculate_number_of_edges(self):
        nr = 0
        for node in self.nodes:
            nr += len(self.nodes[node])

        if not self.oriented:
            if nr // 2 != nr / 2 :
                raise Exception(f"Bug regarding edges!!!")

            nr = int(nr / 2)

        return nr

    def calculate_node_in_degree(self, node):
        if not self.lookup(node):
            raise NodeNotInGraphError(node)

        degree = 0
        for n in self.nodes:
            if node != n:
                if node in self.nodes[n]:
                    degree += 1
        return degree


    def calculate_node_out_degree(self, node):
        if not self.lookup(node):
            raise NodeNotInGraphError(node)
        
        return len(self.nodes[node])
        

    def calculate_node_degree(self, node):
        degree = self.calculate_node_out_degree(node)

        if self.oriented:
            degree += self.calculate_node_in_degree(node)

        return degree

    def get_in_neighbours(self, node):
        if not self.lookup(node):
            raise NodeNotInGraphError(node)
        return {n for n in self.nodes if n in self.nodes[n]}

    def get_out_neighbours(self, node):
        if not self.lookup(node):
            raise NodeNotInGraphError(node)
        return self.nodes[node]

    def get_neighbours(self, node):
        if not self.oriented:
            return self.get_out_neighbours(node)
        return self.get_out_neighbours(node).union(self.get_in_neighbours(node))
        
    def adjacency_test(self, node_a, node_b):
        if node_a not in self.nodes:
            raise NodeNotInGraphError(node_a)
        if node_b not in self.nodes:
            raise NodeNotInGraphError(node_b)

        return node_b in self.nodes[node_a]

    def contract_edge(self, node_a, node_b):
        '''
        Returns the resulted node and the neighbours as proof of work
        '''

        if not self.lookup(node_a):
            raise NodeNotInGraphError(node_a)
        if not self.lookup(node_b):
            raise NodeNotInGraphError(node_b)
        
        if node_b not in self.nodes[node_a]:
            raise VerticeNotInGraph(node_a, node_b)
        
        self.nodes[node_a] = self.nodes[node_a].union(self.nodes[node_b])
        self.nodes[node_a].discard(node_a)

        for node in self.nodes:
            if node != node_b and node_b in self.nodes[node]:
                self.nodes[node].remove(node_b)

                if node != node_a:
                    self.nodes[node].add(node_a)
        
        del self.nodes[node_b]

        return node_a, self.get_neighbours(node_a)
