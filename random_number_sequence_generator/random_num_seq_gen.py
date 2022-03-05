import sys
from datetime import datetime
import random
from random_number_sequence_generator.interfaces.random_num_seq_gen_interface import IRandomNumberSequenceGenerator


class RandomNumberSequenceGenerator(IRandomNumberSequenceGenerator):
    """
    Class of random number sequence generator
    """
    def __init__(self):
        pass

    def next(self):
        return random.randint(-sys.maxsize - 1, sys.maxsize-1)

    def init_with_random_seed(self):
        random.seed(datetime.now().microsecond)

    def init_with_seed(self, seed):
        random.seed(seed)
