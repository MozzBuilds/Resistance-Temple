from flask import Flask, render_template
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