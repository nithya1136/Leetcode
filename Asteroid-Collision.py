class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and a < 0 and s[-1] > 0:
                if s[-1] < -a:
                    s.pop()
                    continue
                elif s[-1] == -a:
                    s.pop()
                break
            else:
                s.append(a)
        return s