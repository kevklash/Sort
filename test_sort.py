from unittest import TestCase

from main import sort


class TestSort(TestCase):

    def test_standard_package(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_bulky_package(self):
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")

    def test_heavy_package(self):
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")

    def test_rejected_package(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")
