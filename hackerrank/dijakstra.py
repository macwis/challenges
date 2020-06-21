import logging
import unittest
import math

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logging.debug('Running ..')


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        self.edges = {}
        for inp, outp, weight in edges:
            if inp not in self.edges.keys():
                self.edges[inp] = {}
            self.edges[inp][outp] = weight
            if outp not in self.edges.keys():
                self.edges[outp] = {}
            self.edges[outp][inp] = weight

    def neighbours(self, vertex):
        return set(self.edges[vertex].keys())

    def min_weight_neighbour(self, vertex, unvisited):
        d = {}
        for u in self.neighbours(vertex):
            if u in unvisited:
                d[u] = self.weight(vertex, u)
        u = min(d, key=d.get)
        return u, d[u]

    def weight(self, vertex_a, vertex_b):
        return self.edges[vertex_a][vertex_b]


class Dijakstra:

    def __init__(self, graph):
        self.graph = graph
        self.unvisited = self.graph.vertices
        self.dist = {}
        self.prev = {}
        for v in self.graph.vertices:
            self.dist[v] = math.inf
            self.prev[v] = None

    def d(self, v):
        return self.dist[v]

    def prev(self, v):
        return self.prev[v]

    def update_table(self, vertex, dist, prev):
        logging.debug(f"Update: {vertex}, {dist}, {prev}")
        self.dist[vertex] = dist
        self.prev[vertex] = prev

    def min_dist_in_table(self):
        filtered = {key: self.dist[key] for key in self.dist.keys()
                 & self.unvisited}
        u = min(filtered, key=filtered.get)
        logging.debug(f"Min. dist found {u}, {self.dist[u]}")
        return u

    def log_table(self):
        logging.debug(f"Unvisited: {self.unvisited}")
        for k, v in self.dist.items():
            logging.debug(f"Table:\t{k}\t{v}\t{self.prev[k]}")

    def solve(self, start):
        self.update_table(start, 0, None)

        while len(self.unvisited) > 0:
            current = self.min_dist_in_table()
            self.unvisited.remove(current)

            for u in self.graph.neighbours(current):
                if u in self.unvisited:
                    weight = self.graph.weight(current, u)
                    alt = self.d(current) + weight
                    if alt < self.d(u):
                        self.update_table(vertex=u, dist=alt, prev=current)
                        self.log_table()

        return self.dist, self.prev


class TestGraph(unittest.TestCase):
    vertices = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    edges = {
        ('A', 'B', 1),
        ('A', 'D', 5),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'E', 10),
        ('C', 'E', 7),
        ('C', 'F', 8),
        ('D', 'F', 1),
        ('F', 'G', 15),
        ('F', 'E', 2),
        ('E', 'G', 1),
    }

    def test_basics(self):
        g = Graph(self.vertices, self.edges)
        neighbours = g.neighbours('A')
        self.assertEqual({'B', 'C', 'D'}, neighbours)
        self.assertEqual(1, g.weight('B', 'A'))
        self.assertEqual(7, g.weight('C', 'E'))
        self.assertEqual(15, g.weight('F', 'G'))
        self.assertEqual(1, g.weight('D', 'F'))
        self.assertEqual(('B', 1), g.min_weight_neighbour('A', g.vertices))
        self.assertEqual(('D', 1), g.min_weight_neighbour('F', g.vertices))


class TestDijakstra(unittest.TestCase):

    def test_solve(self):
        vertices = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        edges = {
            ('A', 'B', 1),
            ('A', 'D', 5),
            ('A', 'C', 3),
            ('B', 'C', 1),
            ('B', 'E', 10),
            ('C', 'E', 7),
            ('C', 'F', 8),
            ('D', 'F', 1),
            ('F', 'G', 15),
            ('F', 'E', 2),
            ('E', 'G', 1),
        }
        g = Graph(vertices, edges)
        di = Dijakstra(g)
        dist, prev = di.solve('A')
        self.assertEqual(
            {'A': 0, 'B': 1, 'C': 2, 'D': 5,
             'E': 8, 'F': 6, 'G': 9}, dist)
        self.assertEqual(
            {'A': None, 'B': 'A', 'C': 'B', 'D': 'A',
             'E': 'F', 'F': 'D', 'G': 'E'}, prev)


if __name__ == "__main__":
    unittest.main(exit=False)
