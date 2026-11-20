
import os
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

from algorithms import nearest_neighbor, branch_and_bound

random.seed(42)
os.makedirs("results", exist_ok=True)


def generate_graph(n):
    """Generate a symmetric weighted graph."""
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            distance = random.randint(5, 100)
            graph[i][j] = distance
            graph[j][i] = distance

    return graph


def test_algorithm(graph, algorithm):
    start = time.perf_counter()
    route, distance = algorithm(graph)
    elapsed = time.perf_counter() - start

    return route, distance, elapsed


# Test the existing sample dataset and larger datasets.
df = pd.read_csv("cities.csv", index_col=0)
small_graph = df.values.tolist()

datasets = {
    "Small (5 cities)": small_graph,
    "Medium (7 cities)": generate_graph(7),
    "Large (9 cities)": generate_graph(9),
    "Larger (11 cities)": generate_graph(11),
}

results = []

print("=" * 65)
print("TSP PERFORMANCE BENCHMARK")
print("=" * 65)

for name, graph in datasets.items():
    approx_route, approx_distance, approx_time = test_algorithm(
        graph, nearest_neighbor
    )

    optimal_route, optimal_distance, optimal_time = test_algorithm(
        graph, branch_and_bound
    )

    print(f"\nDataset: {name}")
    print(f"Nearest Neighbor distance: {approx_distance}")
    print(f"Nearest Neighbor time: {approx_time:.8f} seconds")
    print(f"Branch and Bound distance: {optimal_distance}")
    print(f"Branch and Bound time: {optimal_time:.8f} seconds")

    results.append({
        "Dataset": name,
        "Cities": len(graph),
        "Approximation Distance": approx_distance,
        "Optimal Distance": optimal_distance,
        "Approximation Time (s)": approx_time,
        "Branch and Bound Time (s)": optimal_time,
    })

result_df = pd.DataFrame(results)
result_df.to_csv("results/benchmark_results.csv", index=False)

# Runtime comparison chart
x = range(len(results))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(
    [i - width / 2 for i in x],
    result_df["Approximation Time (s)"],
    width,
    label="Nearest Neighbor"
)
plt.bar(
    [i + width / 2 for i in x],
    result_df["Branch and Bound Time (s)"],
    width,
    label="Branch and Bound"
)

plt.xticks(list(x), result_df["Dataset"], rotation=15)
plt.xlabel("Dataset Size")
plt.ylabel("Execution Time (seconds)")
plt.title("TSP Algorithm Runtime Comparison")
plt.legend()
plt.tight_layout()
plt.savefig("results/runtime_comparison.png", dpi=150)
plt.close()

print("\nBenchmark results saved to results/benchmark_results.csv")
print("Runtime chart saved to results/runtime_comparison.png")
