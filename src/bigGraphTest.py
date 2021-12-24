import unittest

from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_1000_Node(self):
        global g_algo_1000
        g_algo_1000 = GraphAlgo()
        print(g_algo_1000.load_from_json("../data/1000Nodes.json"))

    def est_short_1000(self):
        g_algo_1000.shortest_path(1,2)

    def est_center_1000(self):
        print(g_algo_1000.floidCenter())

    def test_center1000(self):
        print(g_algo_1000.centerPoint())

    def est_10000_Node(self):
        global g_algo_10000
        g_algo_10000 = GraphAlgo()
        print(g_algo_10000.load_from_json("../data/10000Nodes.json"))

    def est_10000_short(self):
        g_algo_10000.shortest_path(1, 2)

    def est_100000_Node(self):
        global g_algo_100_000
        g_algo_100_000 = GraphAlgo()
        print(g_algo_100_000.load_from_json("../data/100000.json"))

    def est_100000_short(self):
        g_algo_100_000.shortest_path(1, 2)


if __name__ == '__main__':
    unittest.main()
