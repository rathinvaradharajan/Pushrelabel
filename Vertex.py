class Vertex:
    """
    A class to represent the vertex in a graph.

    Attributes
    ----------
    h: int
        Height of the vertex.
    e_flow: int
        Effective flow in the vertex. i.e, the inward flow - outward flow.
    """

    def __init__(self, h: int, e_flow: int):
        """
        Create a vertex.

        :param h: the height of the vertex
        :param e_flow: the effective flow in the vertex.
        """
        self.h = h
        self.e_flow = e_flow
