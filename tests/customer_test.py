import unittest
from models.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer('Dwayne', 'Johnson', 'The Rock', 'Active', 'Platinum')

    # The Customer class can take in a 'forename' as STR and return it correctly
    def test_customer_has_forename(self):
        self.assertEqual('Dwayne', self.customer.forename)

    # The Customer class can take in a 'surname' as STR and return it correctly
    def test_customer_has_surname(self):
        self.assertEqual('Johnson', self.customer.surname)

    # The Customer class can take in a 'alias' as STR and return it correctly
    def test_customer_has_alias(self):
        self.assertEqual('The Rock', self.customer.alias)

    # The Customer class can take in a 'membership status' as STR and return it correctly
    def test_customer_has_membership_status(self):
        self.assertEqual('Active', self.customer.membership_status)
    
    # The Customer class can take in a 'membership type' as STR and return it correctly
    def test_customer_has_membership_type(self):
        self.assertEqual('Platinum', self.customer.membership_type)

    # The initial id is set to zero, pre-saving
    def test_customer_initial_id_none(self):
        self.assertEqual(None, self.customer.id)