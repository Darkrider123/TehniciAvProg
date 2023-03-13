from timeit import timeit

from graph import Graph

def parse_file():
    file = None
    with open("facebook_combined.txt", "r") as f:
        file = f.read()

    file = file.split("\n")
    
    file = [(int(line.split(" ")[0]), int(line.split(" ")[1])) for line in file]

    return file


def populate_graph(graph, file):
    for line in file:
        if not graph.lookup(line[0]):
            graph.add_node(line[0])
        if not graph.lookup(line[1]):
            graph.add_node(line[1])
        
        graph.add_edge(line[0], line[1])


def main():
    file = parse_file()
    graph = Graph(oriented=False)
    populate_graph(graph, file)

    #graph.enum_nodes()
    #graph.enum_edges()
    #print(graph.calculate_number_of_nodes())
    #print(graph.calculate_number_of_edges())
    #print(graph.calculate_node_degree(6))
    #print(graph.get_neighbours(6))
    #print(graph.adjacency_test(0, 999))
    #graph.delete_edge(0, 6)
    #graph.delete_node(6)
    


if __name__ == "__main__":
    main()
