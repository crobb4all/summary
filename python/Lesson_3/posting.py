from adress import Adress

class Mailing:
    def __init__(self, to_address, from_address, coast, track):
        self.to_address = to_address
        self.from_address = from_address
        self.coast = int(coast)
        self.track = str(track)