import unittest
from models.customer import Customer
from models.session import Session
from models.booking import Booking


class TestBooking(unittest.TestCase):

    def setUp(self):
        self.customer = Customer('Dwayne', 'Johnson', 'The Rock', 'Active', 'Platinum')
        self.session = Session('Power Punch', 'self-defence', '24-04-2020', '18:00', '19:30', 10)
        self.booking = Booking(self.customer, self.session)

    # The Booking class can take in our Customer obect, and return it after
    def test_booking_has_customer(self):
        self.assertEqual(self.customer, self.booking.customer)

    # The Booking class can take in our Session object, and return it after
    def test_booking_has_session(self):
        self.assertEqual(self.session, self.booking.session)

    # The initial id is set to zero, pre-saving
    def test_booking_initial_id_none(self):
        self.assertEqual(None, self.booking.id)d