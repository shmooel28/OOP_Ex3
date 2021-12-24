import sys

from src.GraphAlgo import GraphAlgo

if __name__ == '__main__':
    graph = GraphAlgo()
    graph.load_from_json(sys.argv[1])
    graph.plot_graph()