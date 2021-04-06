from db.run_sql import run_sql

from models.customer import Customer
from models.session import Session
from models.booking import Booking

import repositories.customer_repository as customer_repository
import repositories.session_repository as session_repository

# Save a new booking
def save(booking):
    sql = 'INSERT INTO bookings(customer_id, session_id) VALUES ( %s, %s) RETURNING id'
    values = [booking.customer.id, booking.session.id]
    results = run_sql( sql, values)
    booking.id = results[0]['id']
    return booking

# Selects all bookings
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

# Selects a singular booking based on booking id
def select(id):
    booking = None
    sql = 'SELECT * FROM bookings WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    if result != None:
        booking = Booking(result['customer'], result['session'], result['id'])
    return booking

# Delete all bookings, currently only used by console.py
def delete_all():
    sql = 'DELETE FROM bookings'
    run_sql(sql)

# Delete one booking
def delete(id):
    sql = 'DELETE FROM bookings WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# Check for duplicate booking, via customer ID matching session ID
def duplicate_check(new_booking):
    bookings = select_all()
    for booking in bookings:
        if booking.customer.id == new_booking.customer.id and booking.session.id == new_booking.session.id: 
            return
    return False