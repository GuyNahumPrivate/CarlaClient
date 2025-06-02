from BenchmarkSimulator.graph_loader import GraphLoader, EntryWaypoint
import networkx as nx

class GraphProvider:

    @staticmethod
    def carla_graph():
        return GraphLoader.load_from('serialized_nodes.pkl', 'serialized_edges.pkl')

    #             1
    #            / \
    #           2   6
    #           |   |
    #           3   7
    #      1    |   |    2
    #           4   8
    #           |   |
    #           5   9
    #            \ /
    #            10
    # The graph has exactly 2 path from node 1 to node 10 with even length
    @staticmethod
    def even_graph():
        even_graph = nx.DiGraph()

        for i in range(1, 11):
            even_graph.add_node(i)

        even_graph.add_edge(1, 2, length=1, entry_waypoint=EntryWaypoint(1))
        even_graph.add_edge(2, 3, length=1, entry_waypoint=EntryWaypoint(1))
        even_graph.add_edge(3, 4, length=1, entry_waypoint=EntryWaypoint(1))
        even_graph.add_edge(4, 5, length=1, entry_waypoint=EntryWaypoint(1))
        even_graph.add_edge(5, 10, length=1, entry_waypoint=EntryWaypoint(1))
        even_graph.add_edge(1, 6, length=1, entry_waypoint=EntryWaypoint(2))
        even_graph.add_edge(6, 7, length=1, entry_waypoint=EntryWaypoint(2))
        even_graph.add_edge(7, 8, length=1, entry_waypoint=EntryWaypoint(2))
        even_graph.add_edge(8, 9, length=1, entry_waypoint=EntryWaypoint(2))
        even_graph.add_edge(9, 10, length=1, entry_waypoint=EntryWaypoint(2))

        return even_graph

    #             1
    #            / \
    #           2   |
    #           |   |
    #           3   |
    #      1    |   |    2
    #           4   |
    #           |   |
    #           5   |
    #            \ /
    #             6
    # Add edges to the graph, so it will have exactly 2 path from node 1 to node 6 with different length
    @staticmethod
    def two_path_graph():
        two_path_graph = nx.DiGraph()

        for i in range(1, 7):
            two_path_graph.add_node(i)

        two_path_graph.add_edge(1, 2, length=100, entry_waypoint=EntryWaypoint(1))
        two_path_graph.add_edge(2, 3, length=100, entry_waypoint=EntryWaypoint(1))
        two_path_graph.add_edge(3, 4, length=100, entry_waypoint=EntryWaypoint(1))
        two_path_graph.add_edge(4, 5, length=100, entry_waypoint=EntryWaypoint(1))
        two_path_graph.add_edge(5, 6, length=100, entry_waypoint=EntryWaypoint(1))
        two_path_graph.add_edge(1, 6, length=1, entry_waypoint=EntryWaypoint(2))

        return two_path_graph
