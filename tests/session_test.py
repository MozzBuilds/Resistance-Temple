import unittest
from models.session import Session

class TestSession(unittest.TestCase):

    def setUp(self):
        self.session = Session('Power Punch', 'self-defence', '24-04-2020', '18:00', '19:30', 10)

    # The Session class can take in a 'name' as STR and return it correctly
    def test_session_has_name(self):
        self.assertEqual('Power Punch', self.session.name)

    # The Session class can take in a 'type of session' by STR return it correctly
    def test_session_has_type(self):
        self.assertEqual('self-defence', self.session.type)

    # The Session class can take in a 'date' as STR and return it correctly
    def test_session_has_date(self):
        self.assertEqual('24-04-2020', self.session.date)

    # The Session class can take in a 'start time' as STR and return it correctly
    def test_session_has_start_time(self):
        self.assertEqual('18:00', self.session.start_time)

    # The Session class can take in an 'end time' as STR and return it correctly
    def test_session_has_end_time(self):
        self.assertEqual('19:30', self.session.end_time)

    # The Session class can take in a 'capacity' as INT and return it correctly
    def test_session_has_capacity(self):
        self.assertEqual(10, self.session.capacity)

    # The initial id is set to zero, pre-saving
    def test_session_has_initial_id_none(self):
        self.assertEqual(None, self.session.id)