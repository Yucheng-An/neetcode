# recursively call dfs

def maxDepth(self, root) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left),maxDepth(root.right))


# bfs
