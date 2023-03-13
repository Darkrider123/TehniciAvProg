class NodeNotInGraphError(ValueError):
    def __init__(self, node):
        super().__init__(f"Node {node} not in graph")

class NodeAlreadyInGraphError(ValueError):
    def __init__(self, node):
        super().__init__(f"Node {node} already in graph")

class EdgeAlreadyPresent(ValueError):
    def __init__(self, node_a, node_b):
        super().__init__(f"Vertice {node_a} -> {node_b} already in graph")

class EdgeNotInGraph(ValueError):
    def __init__(self, node_a, node_b) -> None:
        super().__init__(f"Vertice {node_a} -> {node_b} not in graph")

class ReflexiveEdgeNotAllowed(ValueError):
    def __init__(self, node_a, node_b) -> None:
        super().__init__(f"Node {node_a} same as {node_b}")
