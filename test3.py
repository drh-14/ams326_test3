import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import random

class Q2:
    def __init__(self):
        self.curve = lambda t: abs(np.sin(2 * t))
        self.lengths = np.array([1/10, 1/5, 1/4, 1/3, 1/2, 1])
        
    def solve(self, N = 10000):
        for length in self.lengths:
            hits = 0
            for _ in range(N):
                x1,y1 = random.uniform(-1,1), random.uniform(-1,1)
                theta = random.uniform(0, 2 * np.pi)
                dx, dy = np.cos(theta), np.sin(theta)
                direction = (-1) ** (random.randint(0,1))
                x2, y2 = x1 + direction * dx * length, y1 + direction * dy * length
                for t in np.linspace(0,1, 1000):
                    x = x1 + t * (x2 - x1)
                    y = y1 + t * (y2 - y1)
                    r = np.sqrt(x ** 2 + y ** 2)
                    angle = np.arctan2(y, x)
                    if abs(r - self.curve(angle)) < 0.00001:
                        hits += 1
                        break
            p = hits / N
            print(f"Probability of Crossing for L = {length}: {p}")

if __name__ == "__main__":
    Q2 = Q2()
    Q2.solve()