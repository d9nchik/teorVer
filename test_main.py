from unittest import TestCase

from main import *


class Test(TestCase):
    def test_combination(self):
        self.assertEqual(3, combination(2, 3))
        self.assertEqual(1, combination(5, 5))
        self.assertEqual(6, combination(2, 4))

    def test_theorem_bernuli(self):
        self.assertEqual(35 / 128, theorem_bernuli(4, 7, 0.5))
        self.assertEqual(125 / 3888, theorem_bernuli(3, 5, 1 / 6))

    def test_most_possible_success_variants(self):
        self.assertListEqual([26, 27], most_possible_success_variants(29, 0.9))

    def test_formula_puason(self):
        self.assertAlmostEqual(0.27, formula_puason(1, 1000, 0.002), 2)

    def test_puasson_range(self):
        self.assertAlmostEqual(0.000292, puasson_range(10_000, 0.0003, 11), 6)

    def test_gauss_function(self):
        self.assertAlmostEqual(0.3825, gauss_function(0.29), 4)
        self.assertAlmostEqual(0.1826, gauss_function(1.25), 4)
        self.assertAlmostEqual(0.1826, gauss_function(-1.25), 4)
        self.assertAlmostEqual(0, gauss_function(78))

    def test_local_theorem_of_mavr_laplace(self):
        self.assertAlmostEqual(0.008, local_theorem_of_mavr_laplace(5_000, 10_000, 0.5), 3)
        self.assertAlmostEqual(0, local_theorem_of_mavr_laplace(7_000, 10_000, 0.5))

    def test_laplace_function(self):
        self.assertAlmostEqual(0.47725, laplace_function(2), 5)
        self.assertAlmostEqual(-0.5, laplace_function(-6))

    def test_reverse_laplace_function(self):
        self.assertAlmostEqual(2, reverse_laplace_function(0.47725), 5)
        self.assertEqual(-5, reverse_laplace_function(-0.5))

    def test_integral_theorem_of_mavr_laplace(self):
        self.assertAlmostEqual(0, integral_theorem_of_mavr_laplace(10_000, 6_000, 10_000, 0.5))
        self.assertAlmostEqual(0.9973, integral_theorem_of_mavr_laplace(10_000, 4_850, 5_150, 0.5), 4)

    def test_social_mavr_laplace(self):
        self.assertEqual(6807, social_mavr_laplace(0.01, 0.9))
        self.assertEqual(16_642, social_mavr_laplace(0.01, 0.99))

    def test_three_sigma(self):
        self.assertTupleEqual((7_275, 7_725), three_sigma(30_000, 1 / 4))
