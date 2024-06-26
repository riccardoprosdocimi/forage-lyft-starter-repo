from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, wear_data):
        self.wear_data = wear_data

    def needs_service(self):
        return sum(self.wear_data) >= 3.0
