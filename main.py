from Graph import Graph


def main():
    v = 4
    g = Graph(v)

    g.add_edge(0, 1, 100)
    g.add_edge(0, 2, 100)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 100)
    g.add_edge(2, 3, 100)
    print("Max flow: ", g.get_max_flow(0, 3))

    # v = 6
    # g = Graph(v)
    # g.add_edge(0, 1, 16)
    # g.add_edge(0, 2, 13)
    # g.add_edge(1, 2, 10)
    # g.add_edge(2, 1, 4)
    # g.add_edge(1, 3, 12)
    # g.add_edge(2, 4, 14)
    # g.add_edge(3, 2, 9)
    # g.add_edge(3, 5, 20)
    # g.add_edge(4, 3, 7)
    # g.add_edge(4, 5, 4)

    # print("Max flow: ", g.get_max_flow(0, 5))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
