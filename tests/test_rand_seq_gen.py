import unittest
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator


class TestRandomNumberSequenceGenerator(unittest.TestCase):

    def setUp(self):
        self.gen = RandomNumberSequenceGenerator()
        self.gen.init_with_random_seed()

    def test_numbers_is_int(self):
        numbers = [self.gen.next(), self.gen.next(), self.gen.next(), self.gen.next()]
        for i in range(0, len(numbers)):
            with self.subTest(i=i):
                self.assertEqual(type(numbers[i]), type(1))

    def test_numbers_in_borders(self):
        # tests random nums in sequence
        numbers = [self.gen.next(), self.gen.next(), self.gen.next(), self.gen.next()]
        for i in range(0, len(numbers)):
            with self.subTest(i=i):
                self.assertGreaterEqual(numbers[i], self.gen.min_border)
                self.assertLessEqual(numbers[i], self.gen.max_border)

    def test_same_seeds(self):
        # tests that nums in sequence with same seeds are equal
        numbers = [self.gen.next(), self.gen.next(), self.gen.next(), self.gen.next()]
        for i in range(0, len(numbers)):
            with self.subTest(i=i):
                self.gen.init_with_seed(numbers[i])
                tmp = self.gen.next()
                self.gen.init_with_seed(numbers[i])
                self.assertEqual(tmp, self.gen.next())

    def test_different_seeds(self):
        # tests that nums in sequence with different seeds are not equal
        self.gen.init_with_seed(21)
        tmp = self.gen.next()
        self.gen.init_with_seed(300)
        self.assertNotEqual(tmp, self.gen.next())


if __name__ == '__main__':
    unittest.main()
