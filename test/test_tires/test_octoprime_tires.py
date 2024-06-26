import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_data = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTires(wear_data)
        self.assertTrue(tires.needs_service())

    def test_needs_service_true_2(self):
        wear_data = [1.0, 0.1, 1.0, 0.9]
        tires = OctoprimeTires(wear_data)
        self.assertTrue(tires.needs_service())

    def test_needs_service_true_3(self):
        tire_wear = [0.8, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear_data = [1.0, 0.5, 1.0, 0.4]
        tires = OctoprimeTires(wear_data)
        self.assertFalse(tires.needs_service())

    def test_needs_service_false_2(self):
        wear_data = [0.0, 0.0, 0.0, 0.0]
        tires = OctoprimeTires(wear_data)
        self.assertFalse(tires.needs_service())

    def test_needs_service_false_3(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
