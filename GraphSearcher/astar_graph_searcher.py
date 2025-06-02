from GraphSearcher.graph_searcher import GraphSearcher
import networkx as nx


class AStarGraphSearcher(GraphSearcher):

    def __init__(self, print_total_distance=False):
        self.print_total_distance = print_total_distance

    def find_path(self, graph, source, target, heuristic, weight='length'):
        path = nx.astar_path(graph, source, target, heuristic, weight)

        if self.print_total_distance:
            total_distance = self.calculate_total_distance(graph, path, weight)
            print("Total distance of the path:", total_distance)

        return path



    @staticmethod
    def calculate_total_distance(graph, path, weight='length'):
        total_distance = 0

        for i in range(len(path) - 1):
            # Get the length of the edge between consecutive nodes in the path
            if isinstance(weight, str):
                edge_length = graph[path[i]][path[i + 1]][weight]
            else:
                edge_length = weight(path[i], path[i + 1], graph[path[i]][path[i + 1]])

            total_distance += edge_length

        return total_distance