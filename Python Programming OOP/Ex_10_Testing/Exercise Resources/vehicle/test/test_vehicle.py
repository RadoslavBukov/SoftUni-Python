from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle

class TestVehicle(TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    FUEL = 100
    HORSE_POWER = 200

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__vehicle_init__should_create_proper_obj(self):

        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

# Test Drive Method
        # fuel_needed = self.fuel_consumption * kilometers
        # if self.fuel < fuel_needed:
        #     raise Exception("Not enough fuel")
        # self.fuel -= fuel_needed

    def test__vehicle_drive__with_not_enough_fuel__should_raise_exception(self):
        with self.assertRaises(Exception) as error:                         # When we check exceptions with "with"
            self.vehicle.drive(100)                                         # Operations which raise the exception
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))           # Check the correct error message

    def test__vehicle_drive__with_enough_fuel__should_decrease_fuel(self):
        kilometers = 10
        self.vehicle.drive(kilometers)
        self.vehicle.drive(kilometers)

        expected_result = self.FUEL - 2 * (self.vehicle.fuel_consumption * kilometers)
        actual_result = self.vehicle.fuel
        self.assertEqual(expected_result, actual_result)

    def test__vehicle_drive__with_max_possible_distance__should_decrease_fuel(self):
        kilometers = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(kilometers)
        self.assertEqual(0, self.vehicle.fuel)

# Test Refuel Method
#         if self.fuel + fuel > self.capacity:
#             raise Exception("Too much fuel")
#         self.fuel += fuel

    def test__vehicle_refuel__with_more_fuel_than_capacity__should_raise_exception(self):
        with self.assertRaises(Exception) as error:                         # When we check exceptions with "with"
            self.vehicle.refuel(self.vehicle.capacity + 1)                  # Operations which raise the exception

        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(error.exception))             # Check the correct error message

    def test__vehicle_refuel__with_less_fuel_than_capacity__should_increase_fuel(self):
        fuel = 10
        self.vehicle.fuel -= self.FUEL         # Empty fuel capacity
        self.vehicle.refuel(fuel)
        self.vehicle.refuel(fuel)

        expected_result = (2 * fuel)
        actual_result = self.vehicle.fuel
        self.assertEqual(expected_result, actual_result)

    def test__vehicle_refuel__with_equal_fuel_with_capacity__should_full_the_fuel(self):
        fuel = 20
        self.vehicle.fuel -= fuel

        self.vehicle.refuel(fuel)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test__vehicle_info__should_return_proper_info(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
                          f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        actual_result = self.vehicle.__str__()

        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    main()