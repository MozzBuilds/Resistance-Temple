import pdb
from models.booking import Booking
from models.session import Session
from models.customer import Customer

import repositories.booking_repository as booking_repository
import repositories.session_repository as session_repository
import repositories.customer_repository as customer_repository

booking_repository.delete_all()
session_repository.delete_all()
customer_repository.delete_all()

# Example Customers
customer1 = Customer('Laurence', 'Fishburne', 'Morpheus', 'Active', 'Platinum')
customer_repository.save(customer1)

customer2 = Customer('Carrie-Anne', 'Moss', 'Trinity', 'Active', 'Platinum')
customer_repository.save(customer2)

customer3 = Customer('Keanu', 'Reeves', 'Neo', 'Active', 'Gold')
customer_repository.save(customer3)

customer4 = Customer('Hugo', 'Weaving', 'Agent Smith', 'Inactive', 'None')
customer_repository.save(customer4)

# Example Gym Sessions
session1 = Session('X-Treme Zumba', 'Endurance', '16/04/2021', '14:00', '17:00')
session_repository.save(session1)

session2 = Session('Matter over Mind', 'Strength', '17/04/2021', '09:00', '10:30')
session_repository.save(session2)

# Example Bookings:

booking1 = Booking(customer1, session1)
booking_repository.save(booking1)

booking2 = Booking(customer2, session1)
booking_repository.save(booking2)

booking3 = Booking(customer3, session2)
booking_repository.save(booking3)

pdb.set_trace()