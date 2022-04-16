from Main.Movie import Movie


class Statement:
    # _name = ""
    # _rentals = []

    # ----------------------------------------------------------------------------------------------------------

    # default constructor
    def __init__(self, name):
        self.name = name
        self.rentals = []

    # ----------------------------------------------------------------------------------------------------------

    def addRental(self, rental):
        self.rentals.append(rental)

    # ----------------------------------------------------------------------------------------------------------

    def getName(self):
        return self.name

    # ----------------------------------------------------------------------------------------------------------

    def generate(self):
        self.clearTotal()
        _result = self.header()
        for rental in self.rentals:
            _result = self.rentalLines(_result, rental)
        _result += self.footer()
        return _result

    def footer(self):
        return "You owed " + "{:.1f}".format(self._totalAmount) + "\nYou earned " + str(
            self._frequentRenterPoints) + " frequent renter points\n"

    def rentalLines(self, _result, rental):
        _thisAmount = 0
        _thisAmount = self.detemineAmount(rental)
        self._frequentRenterPoints += 1
        if rental.getMovie().getPriceCode() == Movie.NEW_RELEASE and rental.getDaysRented() > 1:
            self._frequentRenterPoints += 1
        _result += "\t" + rental.getMovie().getTitle() + "\t" + "{:.1f}".format(_thisAmount) + "\n"
        self._totalAmount += _thisAmount
        return _result

    def detemineAmount(self, rental):
        thisAmount=0
        if rental.getMovie().getPriceCode() == Movie.REGULAR:
            thisAmount += 2
            if rental.getDaysRented() > 2:
                thisAmount += (rental.getDaysRented() - 2) * 1.5
        elif rental.getMovie().getPriceCode() == Movie.NEW_RELEASE:
            thisAmount += rental.getDaysRented() * 3
        elif rental.getMovie().getPriceCode() == Movie.CHILDRENS:
            thisAmount += 1.5
            if rental.getDaysRented() > 3:
                thisAmount += (rental.getDaysRented() - 3) * 1.5
        return thisAmount

    def header(self):
        return "Rental Record for " + self.getName() + "\n"

    def clearTotal(self):
        self._totalAmount = 0
        self._frequentRenterPoints = 0

    # ----------------------------------------------------------------------------------------------------------
    def getTotal(self):
        return self._totalAmount

    def getFrequentRenterPoints(self):
        return self._frequentRenterPoints
