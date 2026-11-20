
import time


def calculate_route_distance(route, graph):
    """Calculate total distance of a route, including return to start."""
    total = 0

    for i in range(len(route) - 1):
        total += graph[route[i]][route[i + 1]]

    total += graph[route[-1]][route[0]]
    return total


def nearest_neighbor(graph, start=0):
    """Approximate TSP solution using Nearest Neighbor."""
    n = len(graph)
    unvisited = set(range(n))
    unvisited.remove(start)

    route = [start]
    current = start

    while unvisited:
        next_city = min(
            unvisited,
            key=lambda city: graph[current][city]
        )

        route.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    route.append(start)

    distance = sum(
        graph[route[i]][route[i + 1]]
        for i in range(len(route) - 1)
    )

    return route, distance


def branch_and_bound(graph, start=0):
    """Find the optimal TSP tour using Branch and Bound."""
    n = len(graph)

    best_cost = float("inf")
    best_route = []

    def search(current, visited, path, cost):
        nonlocal best_cost, best_route

        if cost >= best_cost:
            return

        if len(path) == n:
            total_cost = cost + graph[current][start]

            if total_cost < best_cost:
                best_cost = total_cost
                best_route = path[:] + [start]

            return

        for city in range(n):
            if city not in visited:
                new_cost = cost + graph[current][city]

                if new_cost < best_cost:
                    search(
                        city,
                        visited | {city},
                        path + [city],
                        new_cost
                    )

    search(start, {start}, [start], 0)

    return best_route, best_cost


def benchmark(graph, start=0):
    """Compare the two algorithms and measure execution time."""

    start_time = time.perf_counter()
    approx_route, approx_distance = nearest_neighbor(graph, start)
    approx_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    optimal_route, optimal_distance = branch_and_bound(graph, start)
    optimal_time = time.perf_counter() - start_time

    return {
        "approx_route": approx_route,
        "approx_distance": approx_distance,
        "approx_time": approx_time,
        "optimal_route": optimal_route,
        "optimal_distance": optimal_distance,
        "optimal_time": optimal_time,
    }
