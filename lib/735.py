# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res:list[int] = []

        for ast in asteroids:
            if not res or res[-1] < 0 or ast > 0:
                res.append(ast)
                continue

            ast_destroyed = False
            while res and res[-1] > 0:
                comp = abs(res[-1])
                if abs(ast) > comp:
                    _ = res.pop()
                elif abs(ast) < comp:
                    ast_destroyed = True
                    break
                else:
                    ast_destroyed = True
                    _ = res.pop()
                    break

            if not ast_destroyed:
                res.append(ast)

        return res
