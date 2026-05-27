class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adNodeMap = { i:[] for i in range(n) }
        for edge in edges:
            a,b = edge
            adNodeMap[a].append(b)
            adNodeMap[b].append(a)

        visit = set()
        def connect(preNode, node):
            if node in visit:
                return
            visit.add(node)
            for adNode in adNodeMap[node]:
                if preNode == adNode:
                    continue
                connect(node, adNode)
            
        count = 0
        for node in range(n):
            if node in visit:
                continue
            connect(-1, node)
            count += 1
        return count