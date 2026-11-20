
# Travelling Salesperson Problem — Route Planning

## 1. Project Overview

This project implements a route planning system for the
Travelling Salesperson Problem (TSP).

The objective is to find a low-cost tour that visits every
city exactly once and returns to the starting city.

## 2. Objectives

- Implement an exact TSP solution using Branch and Bound.
- Implement an approximate solution using Nearest Neighbor.
- Compare total route distances.
- Measure execution time for different dataset sizes.
- Visualize runtime comparisons using Matplotlib.

## 3. Technologies Used

- Python 3.13
- Pandas
- Matplotlib
- CSV datasets

## 4. Algorithms

### Branch and Bound

Branch and Bound explores possible routes while pruning
partial routes that cannot improve the best known solution.

It finds an optimal tour for the tested instances, assuming
the search completes successfully.

Worst-case time complexity: O(n!)

### Nearest Neighbor Approximation

The algorithm starts at a city and repeatedly visits the
nearest unvisited city. After visiting all cities, it returns
to the starting city.

Time complexity: O(n^2)

This method is fast but does not guarantee an optimal tour.

## 5. Dataset

The input is a weighted distance matrix stored in CSV format.
Each city represents a vertex, and each distance represents
an edge weight.

The current sample dataset contains five cities.
Additional datasets are generated for performance testing.

## 6. Project Structure

TSP_Route_Planning/
├── main.py
├── algorithms.py
├── benchmark.py
├── cities.csv
├── README.md
└── results/
    ├── runtime_chart.png
    ├── benchmark_results.csv
    └── runtime_comparison.png

## 7. Installation

Install the required libraries:

    python -m pip install matplotlib pandas

## 8. Execution

Run the main program:

    python main.py

Run the performance benchmark:

    python benchmark.py

## 9. Performance Analysis

The benchmark tests datasets containing 5, 7, 9, and 11 cities.

Branch and Bound returned distances of 86, 134, 218, and
257 respectively.

Nearest Neighbor returned distances of 86, 199, 257, and
303 respectively.

For the tested datasets, Branch and Bound found tours with
equal or lower costs, but its runtime increased significantly
as the dataset size grew.

The benchmark results are saved in results/benchmark_results.csv.
Runtime charts are saved in the results directory.

## 10. Limitations and Future Scope

- Branch and Bound can become expensive for large instances.
- Nearest Neighbor does not guarantee the optimal tour.
- Current datasets use symmetric distances.
- Future work may include 2-opt local search, better lower
  bounds, asymmetric graphs, and more extensive benchmarking.
