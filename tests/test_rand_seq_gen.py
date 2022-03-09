import unittest
import time
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator


class TestRandomNumberSequenceGenerator(unittest.TestCase):

    def setUp(self):
        self.gen = RandomNumberSequenceGenerator()

    def test_random_in_sequence(self):
        # tests random nums in sequence
        self.assertNotEqual(self.gen.next(), self.gen.next())

    def test_same_seeds(self):
        # tests that nums in sequence with same seeds are equal
        self.gen.init_with_seed(20)
        tmp = self.gen.next()
        self.gen.init_with_seed(20)
        self.assertEqual(tmp, self.gen.next())

    def test_different_seeds(self):
        # tests that nums in sequence with different seeds are not equal
        self.gen.init_with_seed(21)
        tmp = self.gen.next()
        self.gen.init_with_seed(300)
        self.assertNotEqual(tmp, self.gen.next())

    def test_random_seeds(self):
        # tests that init_with_random_seed sets not equal seed
        self.gen.init_with_random_seed()
        tmp = self.gen.next()
        time.sleep(1)
        self.gen.init_with_random_seed()
        self.assertNotEqual(tmp, self.gen.next())
