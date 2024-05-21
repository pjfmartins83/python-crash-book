import unittest
from letter_frequency_counter import letter_frequency_counter

class TestLetterFrequencyCounter(unittest.TestCase):


    def test_letter_frequency_counter_1(self):
        self.assertEqual(letter_frequency_counter('a'), {'a': 1})

    def test_letter_frequency_counter_2(self):
        self.assertEqual(letter_frequency_counter('ab'), {'a': 1, 'b': 1})

    def test_letter_frequency_counter_3(self):
        self.assertEqual(letter_frequency_counter('aab'), {'a': 2, 'b': 1})


if __name__ == '__main__':
    unittest.main()
