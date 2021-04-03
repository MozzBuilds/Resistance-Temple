from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.booking import Booking

import repositories.customer_repository as customer_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint('bookings', __name__)

@bookings_blueprint.route('/bookings')
def bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings=bookings)

# @bookings_blueprint.route('/bookings/<id>')
# def show(id):
#     booking = booking_repository.select_by_id(id)
#     return render_template('bookings/show.html', booking=booking)
# This might be deleted. Might add this to sessions instead

@bookings_blueprint.route('/bookings/new')
def new():
    customers = customer_repository.select_all()
    sessions = session_repository.select_all()
    return render_template('/bookings/new.html', customers=customers, sessions=sessions)
    # This might need to be all_customers=customers and all_sessions=sessions

@bookings_blueprint.route('/bookings', methods=['POST'])
def create():
    bookings = booking_repository.select_all() #This is a list
    customer_id = request.form['customer_id']
    session_id = request.form['session_id']
    customer = customer_repository.select(customer_id)
    session = session_repository.select(session_id)
    new_booking = Booking(customer,session)
    
    for booking in bookings:
        if booking.customer.id == new_booking.customer.id and booking.session.id == new_booking.session.id:
            return 'Booking Already Exists. No new booking has been made'
            # This searches for a duplicate entry, and returns an error string if a duplicate is found
    booking_repository.save(new_booking)
    return redirect('/bookings')
