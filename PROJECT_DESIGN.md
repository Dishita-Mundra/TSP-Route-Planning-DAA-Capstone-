
# Project Design: Travelling Salesperson Problem

## Phase 1: Problem Design and Planning

### 1. Problem Statement

The Travelling Salesperson Problem (TSP) involves finding
a minimum-cost tour that visits every city exactly once
and returns to the starting city.

### 2. Objectives

- Represent cities as vertices in a weighted graph.
- Represent travel distances as weighted edges.
- Implement Branch and Bound for exact route search.
- Implement Nearest Neighbor as an approximation heuristic.
- Compare route costs and execution times.
- Analyse algorithm complexity and scalability.

### 3. Input Data

The input is a CSV distance matrix.

Each row and column represents a city. Each matrix entry
represents the distance between two cities.

The current sample dataset contains five cities.
The graph is undirected and uses symmetric distances.

### 4. Algorithms Selected

**Branch and Bound**

Explores candidate tours and prunes partial paths whose
accumulated cost cannot improve the best complete tour
already found.

**Nearest Neighbor**

Starts from a selected city and repeatedly visits the
nearest unvisited city. It returns to the starting city
after visiting all cities.

### 5. Output

The application displays:

- Route sequence for each algorithm
- Total tour distance
- Execution time
- Runtime comparison chart
- Benchmark results in CSV format

### 6. Complexity Analysis

Nearest Neighbor:
O(n^2) time with the current implementation.

Branch and Bound:
O(n!) worst-case time, with pruning reducing the search
space for some inputs.

The algorithms use different strategies: one searches
for an optimal tour, while the other prioritizes speed.

### 7. Evaluation Plan

Test both algorithms on datasets containing different
numbers of cities.

Compare route costs, verify that each city is visited
exactly once before returning to the start, and record
execution time.

### 8. Limitations

Nearest Neighbor does not guarantee an optimal tour.
Branch and Bound can become expensive for large inputs.
The current implementation uses symmetric distances.
