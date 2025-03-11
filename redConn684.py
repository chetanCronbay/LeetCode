from typing import List

edges = [[1,2],[1,3],[2,3]]

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
        visited = set()
        loop = []
        for n1, n2 in edges:
                if (n1 not in visited) or (n2 not in visited):
                    if n1 not in visited:
                            visited.add(n1)
                            # visited.add(n2)
                    if n2 not in visited:
                        # visited.add(n1)
                        visited.add(n2)
                # elif (n1 or n2) not in visited:
                #         if n1 not in visited:
                #                 visited.add(n1)
                #         else:
                #                 visited.add(n2)
                elif n1 and n2 in visited:
                        loop.append([n1,n2])

        print(loop[-1])
                
findRedundantConnection(edges)