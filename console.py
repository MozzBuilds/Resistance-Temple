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

customer5 = Customer('Gloria', 'Foster', 'The Oracle', 'Active', 'Silver')
customer_repository.save(customer5)

customer6 = Customer('Belinda', 'McClory', 'Switch', 'Active', 'Silver')
customer_repository.save(customer6)

customer7 = Customer('Harold', 'Perrineau', 'Link', 'Active', 'Gold')
customer_repository.save(customer7)

customer8 = Customer('Joe', 'Pantoliano', 'Cypher', 'Inactive', 'None')
customer_repository.save(customer8)

# Example Gym Sessions
session1 = Session('X-Treme Zumba', 'Endurance', '16-04-2021', '14:00', '17:00', 3)
session_repository.save(session1)

session2 = Session('Matter over Mind', 'Strength (Personal)', '17-04-2021', '09:00', '10:30', 1)
session_repository.save(session2)

session3 = Session('Tyre Flippin Good', 'Power', '17-04-2021', '11:00', '13:00', 6)
session_repository.save(session3)

session4 = Session('Vascular Overload', 'Bootcamp', '18-04-2021', '09:00', '14:00', 8)
session_repository.save(session4)

session5 = Session('Freakfull Gainz', 'Yoga', '19-04-2021', '18:00', '20:00', 10)
session_repository.save(session5)

# Example Bookings:
booking1 = Booking(customer1, session1)
booking_repository.save(booking1)

booking2 = Booking(customer2, session1)
booking_repository.save(booking2)

booking3 = Booking(customer3, session1)
booking_repository.save(booking3)

booking4 = Booking(customer1, session2)
booking_repository.save(booking4)

booking5 = Booking(customer1, session3)
booking_repository.save(booking5)

booking6 = Booking(customer1, session4)
booking_repository.save(booking6)

booking7 = Booking(customer1, session5)
booking_repository.save(booking7)

booking8 = Booking(customer5, session3)
booking_repository.save(booking8)

booking9 = Booking(customer5, session4)
booking_repository.save(booking9)

booking10 = Booking(customer5, session5)
booking_repository.save(booking10)

booking11 = Booking(customer6, session3)
booking_repository.save(booking11)

booking12 = Booking(customer6, session4)
booking_repository.save(booking12)

booking13 = Booking(customer7, session5)
booking_repository.save(booking13)

booking14 = Booking(customer7, session4)
booking_repository.save(booking14)

pdb.set_trace()