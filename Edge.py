class Edge:
    def __init__(self, flow: int, capacity: int, u: int, v: int):
        self.flow = flow
        self.capacity = capacity
        self.u = u
        self.v = v
