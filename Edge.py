class Edge:
    """
    A class to represent the edges of a graph.

    Attributes
    ----------
    flow: int
        The current flow in the edge.
    capacity: int
        The max capacity of flow in the edge.
    u: int
        The source vertex of the edge.
    v: int
        The destination vertex of the edge.
    """

    def __init__(self, flow: int, capacity: int, u: int, v: int):
        """
        Create a edge.

        :param flow: the current flow of the edge.
        :param capacity: the capacity of the edge.
        :param u: the source vertex.
        :param v: the destination vertex.
        """
        self.flow = flow
        self.capacity = capacity
        self.u = u
        self.v = v
