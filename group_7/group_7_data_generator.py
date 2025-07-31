import random
import time

class DataGenerator:
    def __init__(self, base=25.0, fluctuation=2.0):
        self.base = base
        self.fluctuation = fluctuation

    def get_value(self):
        pattern = self.base + random.uniform(-self.fluctuation, self.fluctuation)
        # Simulate trend
        trend = random.choice([-0.5, 0, 0.5])
        return round(pattern + trend, 2)

    def get_wild_value(self):
        return round(random.uniform(100, 200), 2)
