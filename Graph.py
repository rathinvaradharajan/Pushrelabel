from Edge import Edge
from Vertex import Vertex


class Graph:
    def __init__(self, v: int):
        self.v = v
        self.ver = [Vertex(0, 0) for i in range(v)]
        self.edges = []

    def add_edge(self, u: int, v: int, capacity: int):
        self.edges.append(Edge(0, capacity, u, v))

    def preflow(self, s: int):
        self.ver[s].h = len(self.ver)
        for e in self.edges:
            if e.u == s:
                e.flow = e.capacity
                self.ver[e.v].e_flow += e.flow
                self.edges.append(Edge(-e.flow, 0, e.v, s))

    def overflow_vertex(self) -> int:
        for i in range(1, len(self.ver) - 1):
            if self.ver[i].e_flow > 0:
                return i
        return -1

    def update_reverse_edge_flow(self, i: int, flow: int):
        u = self.edges[i].v
        v = self.edges[i].u
        for j in range(len(self.edges)):
            if self.edges[j].v == v and self.edges[j].u == u:
                self.edges[j].flow -= flow
                return
        e = Edge(0, flow, u, v)
        self.edges.append(e)

    def push(self, u: int) -> bool:
        for i in range(len(self.edges)):
            if self.edges[i].u == u:
                if self.edges[i].flow == self.edges[i].capacity:
                    continue
                if self.ver[u].h > self.ver[self.edges[i].v].h:
                    flow = min(self.edges[i].capacity - self.edges[i].flow, self.ver[u].e_flow)
                    self.ver[u].e_flow -= flow
                    self.ver[self.edges[i].v].e_flow += flow
                    self.edges[i].flow += flow
                    self.update_reverse_edge_flow(i, flow)
                    return True
        return False

    def relabel(self, u: int):
        mx = 999999
        for i in range(len(self.edges)):
            if self.edges[i].u == u:
                if self.edges[i].flow == self.edges[i].capacity:
                    continue
                if self.ver[self.edges[i].v].h < mx:
                    mx = self.ver[self.edges[i].v].h
                    self.ver[u].h = mx + 1

    def get_max_flow(self, s: int, t: int) -> int:
        self.preflow(s)
        while self.overflow_vertex() != -1:
            u = self.overflow_vertex()
            if self.push(u) is False:
                self.relabel(u)

        return self.ver[len(self.ver) - 1].e_flow
