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
            length = edge_value.length
            entry_waypoint = EntryWaypoint(edge_value.entry_waypoint['road_id'])
            loaded_graph.add_edge(edge_value.u, edge_value.v, length=length, entry_waypoint=entry_waypoint)

        return loaded_graph


class EntryWaypoint:
    def __init__(self, road_id: int):
        self.road_id = road_id
