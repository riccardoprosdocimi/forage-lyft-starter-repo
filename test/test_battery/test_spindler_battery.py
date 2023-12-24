import unittest
from datetime import datetime, date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    # def test_battery_should_be_serviced(self):
    #     today = datetime.today().date()
    #     last_service_date = today.replace(year=today.year - 3)
    #
    #     battery = SpindlerBattery(last_service_date, today)
    #     self.assertTrue(battery.needs_service())
    #
    # def test_battery_should_not_be_serviced(self):
    #     today = datetime.today().date()
    #     last_service_date = today.replace(year=today.year - 1)
    #
    #     battery = SpindlerBattery(last_service_date, today)
    #     self.assertFalse(battery.needs_service())
    #
    # def test_needs_service_true(self):
    #     current_date = date.fromisoformat("2020-05-15")
    #     last_service_date = date.fromisoformat("2018-01-25")
    #     battery = SpindlerBattery(last_service_date, current_date)
    #     self.assertTrue(battery.needs_service())
    #
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2017-01-25")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
