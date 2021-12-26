from unittest import TestCase
from boolean import you_cant_handle_the_truth, booleans_are_easy


class Test(TestCase):
    def test_you_cant_handle_the_truth(self):
        self.assertEqual(you_cant_handle_the_truth(true), bool(1))


    def test_booleans_are_easy(self):
        self.assertEqual(booleans_are_easy(false), bool(0))
