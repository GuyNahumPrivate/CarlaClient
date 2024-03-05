class GraphSearcher:
    """Returns a list of nodes in a path between source and target

        Parameters
        ----------
        G : NetworkX graph

        source : node
           Starting node for path

        target : node
           Ending node for path

        heuristic : function
           A function to evaluate the estimate of the distance
           from the a node to the target.  The function takes
           two nodes arguments and must return a number.
           If the heuristic is inadmissible (if it might
           overestimate the cost of reaching the goal from a node),
           the result may not be a shortest path.

        weight : string or function
           If this is a string, then edge weights will be accessed via the
           edge attribute with this key (that is, the weight of the edge
           joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
           such edge attribute exists, the weight of the edge is assumed to
           be one. If this is a function, the weight of an edge is the value
           returned by the function. The function must accept exactly three
           positional arguments: the two endpoints of an edge and the
           dictionary of edge attributes for that edge. The function must
           return a number or None to indicate a hidden edge.

        Notes
        -----
        Edge weight attributes must be numerical.
        Distances are calculated as sums of weighted edges traversed.

        The weight function can be used to hide edges by returning None.
        So ``weight = lambda u, v, d: 1 if d['color']=="red" else None``
        will find the shortest red path.

        See Also
        --------
        shortest_path, dijkstra_path

        """
    def find_path(self, graph, source, target, heuristic, weight='length'):
        pass
