import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_get_graph(self):
        graph = DiGraph()
        g_algo = GraphAlgo(graph)
        self.assertEqual(graph, g_algo.get_graph())

    def test_load(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/G1.json")
        pos = g_algo.graph.get_node(0).pos
        self.assertEqual(pos, (35.19589389346247, 32.10152879327731, 0.0))

    def test_save(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A0.json")
        g_algo.save_to_json("../data/G1.json_saved")
        g1 = GraphAlgo()
        g1.load_from_json("../data/G1.json_saved")
        self.assertEqual(g1.graph.v_size(), g_algo.graph.v_size())

    def test_center(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/G1.json")
        self.assertEqual(8, g_algo.centerPoint()[0])

    def test_short_path(self):
        g_algo = GraphAlgo()
        file = '../data/A5.json'
        g_algo.load_from_json(file)
        g_algo.get_graph().remove_edge(13, 14)
        g_algo.save_to_json(file + "_edited")
        dist, path = g_algo.shortest_path(1, 7)
        print(dist, path)
        dist, path = g_algo.shortest_path(47, 19)
        print(dist, path)
        dist, path = g_algo.shortest_path(20, 2)
        print(dist, path)
        print(g_algo.shortest_path(2, 20))
        self.assertEqual((17.693921758901507, [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]),
                         g_algo.shortest_path(47, 19))
    # def test_tsp(self):
    # def test_dijkstra(self):


if __name__ == '__main__':
    unittest.main()
