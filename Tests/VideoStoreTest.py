import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from Main.Customer import Customer
from Main.Movie import Movie
from Main.Rental import Rental


class VideoStoreTest(unittest.TestCase):
    def setUp(self):
        print("Starting all the tests.")
        self.customer = Customer("Fred")
        self.newReleaseMovie1 = Movie("New Release Movie 1", Movie.NEW_RELEASE)
        self.newReleaseMovie2 = Movie("New Release Movie 2", Movie.NEW_RELEASE)
        self.childrenMovie = Movie("Children Movie", Movie.CHILDRENS)
        self.regularMovie1 = Movie("Regular Movie 1", Movie.REGULAR)
        self.regularMovie2 = Movie("Regular Movie 2", Movie.REGULAR)
        self.regularMovie3 = Movie("Regular Movie 3", Movie.REGULAR)

    def test_0000_testSingleNewReleaseStatementTotals(self):
        self.customer.addRental(Rental(self.newReleaseMovie1, 3))

        self.customer.statement()
        self.assertEqual(9.0, self.customer.getTotal())
        self.assertEqual(2, self.customer.getFrequentRenterPoints())

    def test_0001_testDualNewReleaseStatementTotals(self):
        self.customer.addRental(Rental(self.newReleaseMovie1, 3))
        self.customer.addRental(Rental(self.newReleaseMovie2, 3))

        self.customer.statement()
        self.assertEqual(18.0, self.customer.getTotal())
        self.assertEqual(4, self.customer.getFrequentRenterPoints())

    def test_0010_testSingleChildrensStatementTotals(self):
        self.customer.addRental(Rental(self.childrenMovie, 3))


        self.customer.statement()
        self.assertEqual(1.5, self.customer.getTotal())
        self.assertEqual(1, self.customer.getFrequentRenterPoints())

    def test_0100_testMultipleRegularStatementTotals(self):
        self.customer.addRental(Rental(self.regularMovie1, 1))
        self.customer.addRental(Rental(self.regularMovie2, 2))
        self.customer.addRental(Rental(self.regularMovie3, 3))

        self.customer.statement()
        self.assertEqual(7.5, self.customer.getTotal())
        self.assertEqual(3, self.customer.getFrequentRenterPoints())

    def test_0101_testMultipleRegularStatementFormat(self):
        self.customer.addRental(Rental(self.regularMovie1, 1))
        self.customer.addRental(Rental(self.regularMovie2, 2))
        self.customer.addRental(Rental(self.regularMovie3, 3))

        self.assertEqual("Rental Record for Fred\n"
                         "\tRegular Movie 1\t2.0\n"
                         "\tRegular Movie 2\t2.0\n"
                         "\tRegular Movie 3\t3.5\n"
                         "You owed 7.5\n"
                         "You earned 3 frequent renter points\n",
                         self.customer.statement())

if __name__ == '__main__':
    unittest.main()