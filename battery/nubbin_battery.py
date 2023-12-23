from battery.battery import Battery
from utils.utils import add_years_to_date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = add_years_to_date(self.last_service_date, 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
