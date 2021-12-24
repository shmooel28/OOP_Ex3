import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_get_mc(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_edge(0,1,1)
        graph.add_edge(0, 2, 1)
        graph.add_edge(0, 3, 1)
        graph.add_edge(0, 4, 1)
        graph.add_edge(0, 5, 1)
        mc = graph.get_mc()
        self.assertEqual(mc, 11)  # add assertion here

    def test_get_node(self):
        graph = DiGraph()
        graph.add_node(0)
        self.assertEqual(0,graph.get_node(0).id)
    def test_add_node(self):
        graph = DiGraph()
        graph.add_node(0)
        self.assertEqual(0, graph.get_node(0).id)
    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 1)
        self.assertEqual(True, graph.add_edge(0, 1, 1))
    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.remove_node(0)
        self.assertEqual(0,graph.v_size())
    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 1)
        graph.remove_edge(0,1)
        self.assertEqual(False,(0,1) in graph.edge_dic)
    def test_e_size(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 1)
        graph.add_edge(0, 3, 1)
        graph.add_edge(0, 4, 1)
        graph.add_edge(0, 5, 1)
        self.assertEqual(5,graph.e_size())
    def test_v_size_test(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        self.assertEqual(6,graph.v_size())
    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 1)
        graph.add_edge(0, 3, 1)
        graph.add_edge(0, 4, 1)
        graph.add_edge(0, 5, 1)
        expected = {0:1}
        actual = graph.all_in_edges_of_node(1)
        self.assertEqual(expected,actual)
    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 1)
        graph.add_edge(0, 3, 1)
        graph.add_edge(0, 4, 1)
        graph.add_edge(0, 5, 1)
        expected = {1:1,2:1,3:1,4:1,5:1}
        actual = graph.all_out_edges_of_node(0)
        self.assertEqual(expected, actual)
    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        expected = len(graph.get_all_v())
        self.assertEqual(expected, 6)

if __name__ == '__main__':
    unittest.main()
