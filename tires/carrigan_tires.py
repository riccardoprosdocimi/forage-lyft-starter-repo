from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, wear_data):
        self.wear_data = wear_data

    def needs_service(self):
        for data in self.wear_data:
            if data >= 0.9:
                return True
        return False
