# 제출 코드 - Runtime 59.65 Memory 66.84
from collections import deque


class ParkingSystem:
    slots = []

    def __init__(self, big: int, medium: int, small: int):
        self.slots = []
        self.slots.append(deque())
        self.slots.append(deque(maxlen=big))
        self.slots.append(deque(maxlen=medium))
        self.slots.append(deque(maxlen=small))

    def addCar(self, carType: int) -> bool:
        if self.slots[carType].maxlen == len(self.slots[carType]):
            return False
        self.slots[carType].append(carType)
        return True


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(0, 0, 2)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
