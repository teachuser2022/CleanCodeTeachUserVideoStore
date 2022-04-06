import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from Main.Customer import Customer
from Main.Movie import Movie
from Main.Rental import Rental


class VideoStoreTest(unittest.TestCase):
    def setUp(self):
        print("Starting all the tests.")
        self.customer = Customer("Fred")

    def test_00_testSingleNewReleaseStatement(self):
        self.customer.addRental(Rental( Movie("The Cell", Movie.NEW_RELEASE), 3))
        self.assertEqual("Rental Record for Fred\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n", self.customer.statement())

    def test_01_testDualNewReleaseStatement(self):
        self.customer.addRental( Rental( Movie("The Cell", Movie.NEW_RELEASE), 3))
        self.customer.addRental( Rental( Movie("The Tigger Movie", Movie.NEW_RELEASE), 3))
        self.assertEqual("Rental Record for Fred\n\tThe Cell\t9.0\n\tThe Tigger Movie\t9.0\nYou owed 18.0\nYou earned 4 frequent renter points\n", self.customer.statement())

    def test_10_testSingleChildrensStatement(self):
        self.customer.addRental( Rental( Movie("The Tigger Movie", Movie.CHILDRENS), 3))
        self.assertEqual("Rental Record for Fred\n\tThe Tigger Movie\t1.5\nYou owed 1.5\nYou earned 1 frequent renter points\n", self.customer.statement())


    def test_11_testMultipleRegularStatement(self):
        self.customer.addRental( Rental( Movie("Plan 9 from Outer Space", Movie.REGULAR), 1))
        self.customer.addRental( Rental( Movie("8 1/2", Movie.REGULAR), 2))
        self.customer.addRental( Rental( Movie("Eraserhead", Movie.REGULAR), 3))
        self.assertEqual("Rental Record for Fred\n\tPlan 9 from Outer Space\t2.0\n\t8 1/2\t2.0\n\tEraserhead\t3.5\nYou owed 7.5\nYou earned 3 frequent renter points\n", self.customer.statement())


if __name__ == '__main__':
    unittest.main()