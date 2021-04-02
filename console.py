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

# Customer 1
# Customer 2
# Customer 3


# Session 1
# Session 2

# Booking 1
# Booking 2
# Booking 3

pdb.set_trace()