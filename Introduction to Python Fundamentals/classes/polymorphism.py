#
# Polymorphism -- object suitability is not determined till the time of use
# inheritance

""" Model for aircrat clights """

class Flight:
    """ A flight with a partiular paseenger aircraft"""
    def __init__(self, number, aircraft):  # to configure an object that already exisits once its created
        # CLASS INVARIENCE, defines -and checks for- requireents on the data coming into the class
        if not number[:2].isalpha():
            raise ValueError("no airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("no airline code in '{}'".format(number))
        if not number[2:].isdigit() or len(number) != 6 :
            raise ValueError("no airline code in '{}'".format(number))

        self._number = number       # prepend _ for objects that are not externally accessible, but will be called through a method is accessible
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]     # fill in structure for all possible seats

    # this is an instance method because it can be call on objects within the class. Method is a function defined within the class (but can not be called?)
    # instance methods must have self as first arg
    def number(self):  
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self,seat,passenger):
        """Allocate a seat to a passenger.
        
        Args:
            seat: A seat designator such as 12C oor 21F.
            passenger: the passenger name.

        Raises:
            ValueError: if the seat is unavailable or invalid
        """
        seat_letter = seat[-1]
        row_text = seat[:-1]

        rows, seat_letters = self._aircraft.seating_plan()

        try:
            row_number = int(row_text)
        except ValueError:
            raise ValueError("invalid row number: "+ row_text)

        if row_number not in rows:
            raise ValueError("invalid row numer: "+ row_text)

        if seat_letter not in seat_letters:
            raise ValueError("invalid seat: "+ row_text)

        if self._seating[row_number][seat_letter] is not None:
            raise ValueError("seat {} already occupied by: {}".format(seat, self._seating[row_number][seat_letter]))
        
        self._seating[row_number][seat_letter] = passenger
         
    def num_available_seats(self):
        return sum( sum(1 for s in row.values() if s is None)
                   for row in self._seating if row is not None)

    # more readable if you ask me
    def num_available_seats2(self):
        count = 0
        for r in self._seating[1:]: #skip the first since by conventrion for the seating rows we started at 1
            count += sum((1 for seat in r.values() if seat is None))
        return count

    def make_boarding_cards(self):
        for pname, seat in sorted(self._passenger_seats()):
            card_printer( pname, seat, self.number(), self._aircraft.model(), self._aircraft.registration())

    def _passenger_seats(self):
        """An iterable list of passenger,seat tuples"""
        rows, seats = self._aircraft.seating_plan()
        for row in rows:
            for seat in seats:
                if self._seating[row][seat] is None:
                    continue
                yield( self._seating[row][seat], "{}{}".format(row,seat))
               

class Aircraft: # this will be a base case but not complete sice it has no seating plan which is unique for each aircraft
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, seats = self.seating_plan()   #seating_plan must be defined in the sub class
        return len(rows) * len(seats)



class AirbusA319(Aircraft):  # AirbusA319 is a subclass of Aircraft -- has everything Aircraft has plus whats new or overriding here
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23), "ABCDEF"


class Boeing777(Aircraft):
    def model(self):
        return "Boing777 A319"

    def seating_plan(self):
        return range(1,56), "ABCDEFGHJK"




def card_printer( pname, seat, flight, model, registration):
    output = "| Name: {} Seat: {} Flight: {} Model: {} Reg: {}".format(pname, seat, flight, model, registration) +' |'
    banner =  '+' + '-' * (len(output) -2) + '+'
    boarder = '|' + ' ' * (len(output) -2) + '|'
    card = '\n'.join([banner, boarder, output, boarder, banner])
    print(card)
    print()


def make_flights():
    f = Flight("BA7581", AirbusA319("G-EUPT"))
    f.allocate_seat('12A','p1')
    f.allocate_seat('12B','p2')
    f.allocate_seat('12C','p3')

    g = Flight("BA7582", Boeing777("G-EUPT"))
    g.allocate_seat('12A','p1')
    g.allocate_seat('12B','p2')
    g.allocate_seat('12C','p3')

    return f, g



if False:
        
    from classes.polymorphism import *
    from pprint import pprint as pp

    f,g = make_flights()

    f.aircraft_model()
    f.airline()
    pp(f._seating)


