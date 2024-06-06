from GraphSearcher.graph_searcher import GraphSearcher
import pickle


class LeanEdge:
    def __init__(self, u, v, length, road_id):
        self.u = u
        self.v = v
        self.length = length
        self.entry_waypoint = {'road_id': road_id}

    @classmethod
    def construct_from(cls, edges, edge) -> ...:
        u = edge[0]
        v = edge[1]
        length = edges[edge]['length']
        road_id = edges[edge]['entry_waypoint'].road_id
        print(road_id)
        return cls(u, v, length, road_id)


class PersistGraphSearcher(GraphSearcher):

    def __init__(self, searcher: GraphSearcher):
        self.searcher = searcher

    @staticmethod
    def is_valid(edges, edge):
        return len((edges[edge].keys())) > 1


    @staticmethod
    def save_to_file(graph, source, target):
        nodes = graph.nodes._nodes
        edges = graph.edges
        lean_edges = {}

        for edge in edges:
            lean_edges[edge] = LeanEdge.construct_from(edges, edge)

        with open('serialized_nodes.pkl', 'wb') as file:
            pickle.dump(nodes, file)

        with open('serialized_edges.pkl', 'wb') as file:
            pickle.dump(lean_edges, file)

    def find_path(self, graph, source, target, heuristic, weight='length'):
        self.save_to_file(graph, source, target)

        return self.searcher.find_path(graph, source, target, heuristic, weight='length')