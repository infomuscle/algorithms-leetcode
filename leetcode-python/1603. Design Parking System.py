# 제출 코드 - Runtime 84.23 Memory 16.91
from collections import deque


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [deque(maxlen=big), deque(maxlen=medium), deque(maxlen=small)]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1].maxlen == len(self.slots[carType - 1]):
            return False

        self.slots[carType - 1].append(carType)

        return True


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(0, 0, 2)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
