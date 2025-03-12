# https://leetcode.com/problems/minimum-genetic-mutation/
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, gene_bank: list[str]) -> int:
        if not gene_bank or endGene not in gene_bank:
            return -1
        bank = set(gene_bank)
        genes = ['A','C','G','T']

        visited = set([startGene])
        q = deque([startGene])
        moves = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return moves
                cur_arr = list(cur)
                for i,orig in enumerate(cur_arr):
                    for gene in genes:
                        if gene == orig:
                            continue
                        cur_arr[i] = gene
                        mutation = ''.join(cur_arr)
                        if mutation in bank and mutation not in visited:
                            q.append(mutation)
                            visited.add(mutation)
                    cur_arr[i] = orig
            moves += 1

        return -1

