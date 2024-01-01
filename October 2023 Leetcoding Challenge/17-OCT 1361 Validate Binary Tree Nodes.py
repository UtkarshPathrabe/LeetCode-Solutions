class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot():
            children = set(leftChild) | set(rightChild)
            rootsList = []
            for i in range(n):
                if i not in children:
                    rootsList.append(i)
            return rootsList
        rootsList = findRoot()
        if len(rootsList) != 1:
            return False
        root = rootsList[0]
        seen, stack = {root}, [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child == -1:
                    continue
                if child in seen:
                    return False
                stack.append(child)
                seen.add(child)
        return len(seen) == n