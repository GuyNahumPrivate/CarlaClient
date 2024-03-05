from GraphSearcher.graph_searcher import GraphSearcher
import networkx as nx


class AStarGraphSearcher(GraphSearcher):
    def find_path(self, graph, source, target, heuristic, weight='length'):
        path = nx.astar_path(graph, source, target, heuristic, weight)
        total_distance = 0
        for i in range(len(path) - 1):
            # Get the length of the edge between consecutive nodes in the path
            if isinstance(weight, str):
                edge_length = graph[path[i]][path[i + 1]][weight]
            else:
                edge_length = weight(path[i], path[i + 1], graph[path[i]][path[i + 1]])

            total_distance += edge_length

        print("Total distance of the path:", total_distance)

        return path
