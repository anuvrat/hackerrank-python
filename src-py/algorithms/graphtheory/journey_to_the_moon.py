class WeightedQuickUnion(object):
    def __init__(self, size):
        self.group_count = self.size= size
        self.group = [i for i in range(size)]
        self.tree_size = [1] * size

    def union(self, child, parent):
        child_root = self.find(child)
        parent_root = self.find(parent)

        if child_root == parent_root: return 1, 1, 1

        # push the smaller tree into the larger tree to reduce tree height
        parent_tree_size = self.tree_size[parent_root]
        child_tree_size = self.tree_size[child_root]
        new_tree_size = self.tree_size[parent_root] + self.tree_size[child_root]
        if self.tree_size[child_root] < self.tree_size[parent_root]:
            self.group[child_root] = self.group[parent_root]
            self.tree_size[parent_root] = new_tree_size
        else:
            self.group[parent_root] = self.group[child_root]
            self.tree_size[child_root] = new_tree_size
        self.group_count -= 1

        return child_tree_size, parent_tree_size, new_tree_size

    def find(self, element):
        while self.group[element] != element:
            self.group[element] = self.group[self.group[element]]
            element = self.group[element]
        return element

    def get_count_of_groups(self):
        return self.group_count

    def get_groups(self):
        return self.group

    def connected(self, element_a, element_b):
        return self.find(element_a) == self.find(element_b)

    def get_size_of_group(self, element):
        return self.tree_size[element]

if __name__ == '__main__':
    n, i = map(int, input().strip().split())

    uf = WeightedQuickUnion(n)
    for _ in range(i):
        a, b = map(int, input().strip().split())
        uf.union(a, b)

    groups = set(uf.find(_) for _ in range(n))
    size_of_groups = [uf.get_size_of_group(i) for i in groups]
    total_size = n

    total_ways = 0
    for i in range(len(groups)):
        total_size -= size_of_groups[i]
        total_ways += (size_of_groups[i] * total_size)

    print(total_ways)
