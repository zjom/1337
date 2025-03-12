# https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        def build_graph(equations: list[list[str]], values: list[float]) -> dict[str,dict[str, float]]:
            graph:dict[str,dict[str, float]] = {}
            for i in range(len(values)):
                u,v = equations[i]
                value = values[i]

                if u not in graph:
                    graph[u] = {}
                graph[u][v] = value
                if v not in graph:
                    graph[v] = {}
                graph[v][u] = 1/value

            return graph

        def get_path_weight(start: str, end:str, visited: set[str], graph: dict[str,dict[str,float]]) -> float:
            if start not in graph:
                return -1

            if end in graph[start]:
                return graph[start][end]

            visited.add(start)
            for k,v in graph[start].items():
                if k not in visited:
                    productWeight = get_path_weight(k, end, visited, graph)
                    if productWeight != -1:
                        return v * productWeight

            return -1

        graph = build_graph(equations, values)
        result:list[float] = [-1 for _ in range(len(queries))]
        for i in range(len(queries)):
            start, end = queries[i]
            result[i] = get_path_weight(start, end, set(), graph)

        return result
