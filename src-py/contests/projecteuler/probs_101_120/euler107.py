class WeightedQuickUnion(object):
    def __init__(self, size):
        self.group_count = self.size = size
        self.group = [i for i in range(size)]
        self.tree_size = [1] * size

    def union(self, child, parent):
        """ Complexity = O(lg n) """
        child_root = self.find(child)
        parent_root = self.find(parent)

        if child_root == parent_root: return

        # push the smaller tree into the larger tree to reduce tree height
        new_tree_size = self.tree_size[parent_root] + self.tree_size[child_root]
        if self.tree_size[child_root] < self.tree_size[parent_root]:
            self.group[child_root] = self.group[parent_root]
            self.tree_size[parent_root] = new_tree_size
        else:
            self.group[parent_root] = self.group[child_root]
            self.tree_size[child_root] = new_tree_size
        self.group_count -= self.group_count

    def find(self, element):
        """ Complexity = O(lg n) """
        while self.group[element] != element:
            self.group[element] = self.group[self.group[element]]
            element = self.group[element]
        return element

    def get_count_of_groups(self):
        return self.group_count

    def connected(self, element_a, element_b):
        """ Complexity = O(lg n) """
        return self.find(element_a) == self.find(element_b)


class Edge(object):
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


if __name__ == '__main__':
    vertices_count, edges_count = map(int, input().split())

    graph_matrix = [[None] * vertices_count for i in range(vertices_count)]
    edges = [] * edges_count

    for _ in range(edges_count):
        a, b, c = map(int, input().split())
        a, b = (a - 1, b - 1) if a < b else (b - 1, a - 1)
        if graph_matrix[a][b] is None:
            e = Edge(a, b, c)
            graph_matrix[a][b] = e
            edges.append(e)
        elif (graph_matrix[a][b]).weight > c:
            graph_matrix[a][b].weight = c

    edges.sort(key=lambda e: e.weight)

    cost = 0
    qu = WeightedQuickUnion(vertices_count)
    for e in edges:
        if qu.find(e.v1) != qu.find(e.v2):
            qu.union(e.v1, e.v2)
            cost += e.weight

    print(cost)
