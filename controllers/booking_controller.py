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
# This might be deleted. Might add this to sessions instead, or just allow edits/deletes from the select_all route

@bookings_blueprint.route('/bookings/new')
def new():
    customers = customer_repository.select_all()
    sessions = session_repository.select_all()
    return render_template('/bookings/new.html', customers=customers, sessions=sessions)
    # This might need to be all_customers=customers and all_sessions=sessions

@bookings_blueprint.route('/bookings', methods=['POST'])
def create():
    customer_id = request.form['customer_id']
    session_id = request.form['session_id']
    customer = customer_repository.select(customer_id)
    session = session_repository.select(session_id)

    new_booking = Booking(customer,session)

    if booking_repository.membership_status_check(customer_id) == True:
        if booking_repository.duplicate_check(new_booking) == True:
            return 'Booking Already Exists. No new booking has been made'
        else:
            booking_repository.save(new_booking)
            return redirect('/bookings')
    else:
        return 'The customer has an inactive membership and cannot be booked at this time'


# Delete a booking
@bookings_blueprint.route('/bookings/<id>/delete', methods=['POST'])
def delete(id):
    booking_repository.delete(id)
    return redirect ('/bookings')