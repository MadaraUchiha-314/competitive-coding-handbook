class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def root(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def find(self, a, b):
        return self.root(a) == self.root(b)

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if self.size[root_a] < self.size[root_b]:
            self.parent[root_a] = self.parent[root_b]
            self.size[root_b] += self.size[root_a]
        else:
            self.parent[root_b] = self.parent[root_a]
            self.size[root_a] += self.size[root_b]