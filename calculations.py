import statistics

#Mean = Sum of all Values / Number of Values
#Return the sample standard deviation (the square root of the sample variance)

def calculate_time_statistics(experiment_results, heuristic):

    elapsed_time = []

    for state_result in experiment_results:
        result = state_result["results"][heuristic]
        elapsed_time.append(result["elapsed_time"])

    return {
        "mean": statistics.mean(elapsed_time),
        "standard_deviation": statistics.stdev(elapsed_time)
        if len(elapsed_time) > 1
        else 0.0
    }

def calculate_node_statistics(experiment_results, heuristic):

    expanded_nodes = []

    for state_result in experiment_results:
        result = state_result["results"][heuristic]
        expanded_nodes.append(result["expanded_nodes"])

    return {
        "mean": statistics.mean(expanded_nodes),
        "standard_deviation": statistics.stdev(expanded_nodes)
        if len(expanded_nodes) > 1
        else 0.0
    }

def calculate_experiment_statistics(experiment_results):

    number_of_searches = len(experiment_results)

    heuristic = [
        "manhattan",
        "hamming",
        "zero_heuristic"
    ]

    all_statistics = {}

    for heuristic in heuristic:
        all_statistics[heuristic] = {
            "time": calculate_time_statistics(
                experiment_results,
                heuristic
            ),
            "nodes": calculate_node_statistics(
                experiment_results,
                heuristic
            )
        }

    return {
        "all_statistics": all_statistics,
        "number_of_searches": number_of_searches
    }

def print_calculation_results(statistics_results):
    print("\n" + "=" * 70)
    print("8 Puzzle A* Search Summary")
    print("=" * 70)

    number_of_searches = statistics_results["number_of_searches"]
    print(f"Number of searches: {number_of_searches}")

    heuristic_name = {
        "manhattan": "Manhattan distance",
        "hamming": "Hamming distance",
        "zero_heuristic": "Zero Heuristic"
    }

    all_statistics = statistics_results["all_statistics"]

    for heuristic, results in all_statistics.items():
        time_result = results["time"]
        node_result = results["nodes"]

        print()
        print(f"-" * 70)
        print(f"{heuristic_name[heuristic]}")
        print("-" * 70)

        print("Computation time:")
        print(f"    Mean: {time_result['mean']:.6f} seconds")
        print(f"    Standard deviation: "
            f"{time_result['standard_deviation']:.6f} seconds"
        )

        print(f"\nMemory effort (expanded nodes):")
        print(f"    Mean: {node_result['mean']:.2f} nodes")
        print(f"    Standard deviation: " 
            f"{node_result['standard_deviation']:.2f} nodes"
        )

    print("\n" + "=" * 70)