from db.run_sql import run_sql

from models.customer import Customer
from models.session import Session
from models.booking import Booking

import repositories.customer_repository as customer_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = 'INSERT INTO bookings(customer_id, session_id) VALUES ( %s, %s) RETURNING id'
    values = [booking.customer.id, booking.session.id]
    results = run_sql( sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []

    sql = 'SELECT * FROM bookings'
    results = run_sql(sql)

    for row in results:
        customer = customer_repository.select(row['customer_id'])
        session = session_repository.select(row['session_id'])
        booking = Booking(customer, session, row['id'])
        bookings.append(booking)
    return bookings

def delete_all():
    sql = 'DELETE FROM bookings'
    run_sql(sql)