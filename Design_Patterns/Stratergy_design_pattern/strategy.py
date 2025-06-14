#For more detailed implementation refer the video by Shreyansh

from abc import abstractmethod, ABC 

#Define the Strtergy Interface
class DriveStrategy():
    @abstractmethod
    def drive(self):
        pass

#Define the concrete stratergies
class NormalDriveStratergy(DriveStrategy):
    def drive(self):
        print("Noral Driving behaviour")

class SpecialDriveStratergy(DriveStrategy):
    def drive(self):
        print("Special Drive Stratergy")

class Vehicle():
    def __init__(self, driveStratergy):
        self.driveSt = driveStratergy

    def drive(self):
        self.driveSt.drive()

class PassengerVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStratergy())

class offRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStratergy())

class SportVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStratergy())


if __name__ == "__main__":
    pv = PassengerVehicle()
    pv.drive()  # Output: Normal driving behavior

    ov = offRoadVehicle()
    ov.drive()  # Output: Special performance driving

    sv = SportVehicle()
    sv.drive()  # Output: Special performance driving