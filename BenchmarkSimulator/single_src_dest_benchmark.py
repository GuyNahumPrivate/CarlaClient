class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SingleSrcDestBenchmark:
    def run(self, graph, source, destination, total_path_calculation, base_searcher, evaluate_searcher):
        total_travel_time = 0
        total_evaluate_travel_time = 0
        upper_bound = 1

        for i in range(1, total_path_calculation + 1):
            selected_path = base_searcher.find_path(graph, source, destination, None)
            travel_time = self.calculate_path_length(graph, selected_path)
            total_travel_time += travel_time

            selected_path_evaluate = evaluate_searcher.find_path(graph, source, destination, None)
            factored_travel_time = self.calculate_path_length(graph, selected_path_evaluate)
            total_evaluate_travel_time += factored_travel_time

            upper_bound = max(upper_bound, factored_travel_time / travel_time)

        print(f"{BColors.OKBLUE} Evaluate Searcher:")
        print(f"{BColors.OKBLUE} Congestion Level: {evaluate_searcher.roads_congestion.get_max_congestion()}")
        print(f"{BColors.OKBLUE} Average Travel Time: {total_evaluate_travel_time / total_path_calculation}")
        print(f"{BColors.OKGREEN} Base Searcher:")
        print(f"{BColors.OKGREEN} Congestion Level: {base_searcher.roads_congestion.get_max_congestion()}")
        print(f"{BColors.OKGREEN} Average Travel Time: {total_travel_time / total_path_calculation}")
        print(f"{BColors.BOLD}{BColors.OKCYAN} Upper Bound: {upper_bound}")

    @staticmethod
    def calculate_path_length(graph, path, weight='length'):
        total_distance = 0
        for n in range(len(path) - 1):
            total_distance += graph[path[n]][path[n + 1]][weight]

        return total_distance
