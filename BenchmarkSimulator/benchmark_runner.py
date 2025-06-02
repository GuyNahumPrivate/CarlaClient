from searcher_provider import SearcherProvider
from graph_provider import GraphProvider
from BenchmarkSimulator.single_src_dest_benchmark import SingleSrcDestBenchmark

carla_graph = GraphProvider.carla_graph()
source = 27
destination = 104
benchmark = SingleSrcDestBenchmark()


def base_searcher(max_capacity=10):
    # return SearcherProvider.a_a_star_searcher(max_capacity)
    return SearcherProvider.a_random_k_shortest_path_searcher(max_capacity)

# The higher the factor will be, the less the congestion level will be and the average travel time will be higher:
print("\ndifferent congestion_tolerance")

print("\nRunning with congestion_tolerance: 100")
benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))

print("\nRunning with congestion_tolerance: 50")
benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=50))

print("\nRunning with congestion_tolerance: 10")
benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=10))

print("\nRunning with congestion_tolerance: 5")
benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=5))

print("\nRunning with congestion_tolerance: 0")
benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=0))

# The more load on the roads,
# we might reach the limit of the traffic distribution, and the congestion level improvement will decrease
print("\ndifferent loads")

print("\nRunning with load: 50")
benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))

print("\nRunning with load: 150")
benchmark.run(carla_graph, source, destination, 150, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))

print("\nRunning with load: 500")
benchmark.run(carla_graph, source, destination, 500, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))

print("\nRunning with load: 1500")
benchmark.run(carla_graph, source, destination, 1500, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))

# depends on the graph, we might get improvements without effecting the average travel time:
print("\n different graphs")

print("\nRunning even graph")
benchmark.run(GraphProvider.even_graph(), 1, 10, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))

print("\nRunning two paths graph")
benchmark.run(GraphProvider.two_path_graph(), 1, 6, 50, base_searcher(), SearcherProvider.a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=100))
