
import unittest

from algorithms import nearest_neighbor, branch_and_bound


class TestTSPAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0],
        ]

    def check_route(self, route, distance):
        n = len(self.graph)

        self.assertEqual(route[0], 0)
        self.assertEqual(route[-1], 0)
        self.assertEqual(len(route), n + 1)
        self.assertEqual(set(route[:-1]), set(range(n)))

        actual_distance = sum(
            self.graph[route[i]][route[i + 1]]
            for i in range(len(route) - 1)
        )
        self.assertEqual(actual_distance, distance)

    def test_nearest_neighbor(self):
        route, distance = nearest_neighbor(self.graph)
        self.check_route(route, distance)

    def test_branch_and_bound(self):
        route, distance = branch_and_bound(self.graph)
        self.check_route(route, distance)

    def test_optimal_not_worse_than_approximation(self):
        _, approx_distance = nearest_neighbor(self.graph)
        _, optimal_distance = branch_and_bound(self.graph)

        self.assertLessEqual(optimal_distance, approx_distance)


if __name__ == "__main__":
    unittest.main()
