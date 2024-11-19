# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def simplifyPath(self, path: str) -> str:
        acc:list[str] = []

        def aux(p: list[str]) -> None:
            if len(p) == 0:
                return
            hd,tl = p[0], p[1:]
            match hd:
                case '.':
                    return aux(tl)
                case '/':
                    return aux(tl)
                case '..':
                    if len(acc) >= 1:
                        _ = acc.pop()
                    return aux(tl)
                case '':
                    return aux(tl)
                case _:
                    acc.append(hd)
                    return aux(tl)
        aux(path.split('/'))
        return '/'+'/'.join(acc)
