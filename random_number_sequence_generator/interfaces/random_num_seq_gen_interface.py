from abc import ABCMeta, abstractmethod


class IRandomNumberSequenceGenerator:
    """
    Random number sequence generator interface
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def next(self):
        """
        Method gets next element of sequence

        :return: Element of random sequence (int)
        """
        raise NotImplementedError

    @abstractmethod
    def init_with_random_seed(self):
        """
        Method init generator with random seed
        """
        raise NotImplementedError

    @abstractmethod
    def init_with_seed(self, seed):
        """ Method init generator with received seed

        :param seed: number which will be new seed
        """

        raise NotImplementedError
