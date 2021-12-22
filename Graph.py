from Edge import Edge
from Vertex import Vertex


class Graph:
    """
    A class to represent a directed graph in which max flow can be computed using the push relabel algorithm.

    Attributes
    ----------
    v: int
        Count of vertices in the graph.
    ver: [Vertex]
        List of vertices in the graph.
    edges: [Edge]
        List of edges in the graph.

    Methods
    -------
    add_edges(u: int, v: int, capacity: int):
        add edge to the graph.

    preflow(s: int):
        calculate the preflow in the graph from source s.

    overflow_vertex() -> int:
        get the vertex with overflow.

    update_reverse_edge_flow(i: int, flow: int):
        update residual edge between vertices into the edge set.

    push(u: int):
        push flow from vertex u.

    relabel(u: int):
        relabel vertex u.

    get_max_flow(s: int, t: int) -> int:
        get the max flow between the source and destiantion in the graph.
    """

    def __init__(self, v: int):
        """
        Create a graph with the given count of vertices.

        :param v: the count of vertices in the graph.
        """
        self.v = v
        self.ver = [Vertex(0, 0) for i in range(v)]
        self.edges = []

    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add a edge to the graph.

        :param u: the source vertex of the graph.
        :param v: the destination vertex of the graph.
        :param capacity: the capacity of the edge.
        :return: void
        """
        self.edges.append(Edge(0, capacity, u, v))

    def preflow(self, s: int):
        """
        Calculate the preflow in the graph.

        :param s: the source vertex.
        :return: void
        """
        self.ver[s].h = len(self.ver)
        for e in self.edges:
            if e.u == s:
                e.flow = e.capacity
                self.ver[e.v].e_flow += e.flow
                self.edges.append(Edge(-e.flow, 0, e.v, s))

    def overflow_vertex(self) -> int:
        """
        Get a vertex which has overflow. i.e, vertex with effective flow > 0.

        :return: the vertex if exits, else  -1.
        """
        for i in range(1, len(self.ver) - 1):
            if self.ver[i].e_flow > 0:
                return i
        return -1

    def update_reverse_edge_flow(self, i: int, flow: int):
        """
        Update the residual flow between vertices to the edge list.

        :param i: the edge's index.
        :param flow: the flow through the edge.
        :return: void.
        """
        u = self.edges[i].v
        v = self.edges[i].u
        for j in range(len(self.edges)):
            if self.edges[j].v == v and self.edges[j].u == u:
                self.edges[j].flow -= flow
                return
        e = Edge(0, flow, u, v)
        self.edges.append(e)

    def push(self, u: int) -> bool:
        """
        Push flow from the vertex u.

        :param u: the vertex to push from.
        :return: if the push operation is possible.
        """
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
        """
        Increase the height of the vertex u to enable flow.

        :param u: the vertex to relabel.
        :return: void.
        """
        mx = 999999
        for i in range(len(self.edges)):
            if self.edges[i].u == u:
                if self.edges[i].flow == self.edges[i].capacity:
                    continue
                if self.ver[self.edges[i].v].h < mx:
                    mx = self.ver[self.edges[i].v].h
                    self.ver[u].h = mx + 1

    def get_max_flow(self, s: int, t: int) -> int:
        """
        Get the max flow between the source and destination in the graph.

        :param s: the source vertex.
        :param t: the destination vertex.
        :return: the max flow in the graph.
        """
        self.preflow(s)
        while self.overflow_vertex() != -1:
            u = self.overflow_vertex()
            if self.push(u) is False:
                self.relabel(u)

        return self.ver[len(self.ver) - 1].e_flow
