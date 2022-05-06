import sys
import random
from datetime import datetime


class RandomNumberSequenceGenerator:
    """
    Class of random number sequence generator
    """

    def __init__(self):
        self.seed = None
        self.min_border = -sys.maxsize - 1
        self.max_border = sys.maxsize - 1

    def next(self):
        return random.randint(self.min_border, self.max_border)

    def init_with_random_seed(self):
        self.seed = datetime.now().microsecond
        random.seed(self.seed)

    def init_with_seed(self, seed):
        self.seed = seed
        random.seed(seed)
