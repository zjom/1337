# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict

class UF:
    def __init__(self, N:int) -> None:
        self.parents: list[int] = list(range(N))

    def union(self, child: int, parent:int) -> None:
        self.parents[self.find(child)] = self.find(parent)
        return

    def find(self, x:int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UF(len(accounts))

        ownership:dict[str,int] = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        ans:dict[int,list[str]] = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]]+sorted(emails) for i, emails in ans.items()]
