# model for airplane flight

class Flight:

    def __init__(self, number, airplane, brand, price, economy, first_class):
        if not number[:2].isalpha():
            raise ValueError(f"No flight code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid flight code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Wrong route number '{number}'")

        self._number = number
        self._airplane = airplane
        rows, seats = self._airplane.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        self._brand = brand
        self._price = price
        self._economy = economy
        self._first_class = first_class

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def airplane_model(self):
        return self._airplane.model()

    def brand(self):
        return self._brand

    def price(self):
        return self._price

    def economy(self):
        return self._economy

    def first_class(self):
        return self._first_class


class Airplane:

    def __init__(self, registration, model, num_rows, num_seats_per_row, seat_number):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        self._seat_number = seat_number

    def registration(self):
        return self._registration

    def model(self,):
        return self._model, 'Boeing', 'Airbus'

    def seat_number(self):
        return self._seat_number

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                'ABCDEFGHJK'[:self._num_seats_per_row])


air_plane = Airplane("R-Sibiu", "Boeing 737", num_rows=22, num_seats_per_row=6, seat_number=69)
flight_object = Flight('RO991', Airplane('R-CLUJ', 'Boeing 737', num_rows=22, num_seats_per_row=6, seat_number=69, ))
flight_object_21 = Flight("RO992", Airplane("R-BUC", "Airbus A300", num_rows=22, seat_number=None))

print("Aeroplane Registration:", air_plane.registration())
print("Aeroplane Seating plan: ", air_plane.seating_plan())
print("Aeroplane Model: ", flight_object.airplane_model())
print("Aeroplane Seat: ", flight_object._seating())

