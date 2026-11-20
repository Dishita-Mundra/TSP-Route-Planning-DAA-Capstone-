import pandas as pd
import matplotlib.pyplot as plt
from algorithms import benchmark

# -----------------------------
# Read Distance Matrix
# -----------------------------
df = pd.read_csv("cities.csv", index_col=0)

graph = df.values.tolist()
cities = list(df.index)

# -----------------------------
# Run Algorithms
# -----------------------------
result = benchmark(graph)

# -----------------------------
# Display Results
# -----------------------------
print("=" * 50)
print("Travelling Salesperson Problem")
print("=" * 50)

print("\nBranch and Bound (Optimal)")
print("--------------------------")
print("Route : ", " -> ".join(cities[i] for i in result["optimal_route"]))
print("Distance :", result["optimal_distance"])
print("Execution Time :", round(result["optimal_time"], 6), "seconds")

print("\nNearest Neighbor (Approximation)")
print("--------------------------------")
print("Route :", " -> ".join(cities[i] for i in result["approx_route"]))
print("Distance :", result["approx_distance"])
print("Execution Time :", round(result["approx_time"], 6), "seconds")

# -----------------------------
# Runtime Comparison Chart
# -----------------------------
algorithms = ["Branch & Bound", "Nearest Neighbor"]
times = [
    result["optimal_time"],
    result["approx_time"]
]

plt.figure(figsize=(6,4))
plt.bar(algorithms, times)
plt.title("Execution Time Comparison")
plt.ylabel("Time (seconds)")
plt.savefig("results/runtime_chart.png")

print("\nRuntime chart saved inside results folder.")