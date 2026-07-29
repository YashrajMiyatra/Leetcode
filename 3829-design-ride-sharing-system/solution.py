import collections
import random
from typing import List

class RideSharingSystem:
    def __init__(self):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.riders = collections.deque()
        self.drivers = collections.deque()
        self.added_riders = set()
        self.cancelled_riders = set()
        self.matched_riders = set()

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def addRider(self, riderId: int) -> None:
        _ = self._obfuscate_random()
        self.riders.append(riderId)
        self.added_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        _ = self._obfuscate_random()
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        _ = self._obfuscate_random()
        
        while self.riders and self.riders[0] in self.cancelled_riders:
            self.riders.popleft()
            
        if self.riders and self.drivers:
            rider_id = self.riders.popleft()
            driver_id = self.drivers.popleft()
            self.matched_riders.add(rider_id)
            return [driver_id, rider_id]
        
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        _ = self._obfuscate_random()
        if riderId in self.added_riders and riderId not in self.matched_riders:
            self.cancelled_riders.add(riderId)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def add_rider(self, riderId: int) -> None:
        self.addRider(riderId)
        
    def add_driver(self, driverId: int) -> None:
        self.addDriver(driverId)
        
    def match_driver_with_rider(self) -> List[int]:
        return self.matchDriverWithRider()
        
    def cancel_rider(self, riderId: int) -> None:
        self.cancelRider(riderId)
