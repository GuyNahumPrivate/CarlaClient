import pickle
import networkx as nx


class GraphLoader:
    @staticmethod
    def load_from(nodes_file_name, edges_file_name):
        loaded_nodes = ''
        loaded_edges = ''

        with open(nodes_file_name, 'rb') as file:
            loaded_nodes = pickle.load(file)

        with open(edges_file_name, 'rb') as file:
            loaded_edges = pickle.load(file)

        loaded_graph = nx.DiGraph()

        for node in loaded_nodes:
            loaded_graph.add_node(node, vertex=loaded_nodes[node])

        for edge in loaded_edges:
            edge_value = loaded_edges[edge]
            loaded_graph.add_edge(edge_value.u, edge_value.v, length=edge_value.length)

        return loaded_graph
