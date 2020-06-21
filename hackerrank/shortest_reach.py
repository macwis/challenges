import logging
import math

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
        if vertex in self.edges.keys():
            return set(self.edges[vertex].keys())
        else:
            return set()

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


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        pairs = []
        for i in range(m):
            pairs.append([int(x) for x in input().split()])
        vertices = tuple((i for i in range(1, n+1)))
        edges = {(x, y, 6) for x, y in pairs}
        g = Graph(vertices, edges)
        s = int(input())
        #print(vertices, edges, s)
        di = Dijakstra(g)
        dist, prev = di.solve(s)
        for k in sorted(dist):
            v = dist[k]
            if v == math.inf:
                print(-1, end=' ')
            elif v != 0:
                print(v, end=' ')
        print()
