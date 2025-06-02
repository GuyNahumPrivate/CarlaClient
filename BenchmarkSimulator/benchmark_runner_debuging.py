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

benchmark.run(carla_graph, source, destination, 50, base_searcher(), SearcherProvider.a_a_star_searcher())
