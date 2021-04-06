from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

from datetime import date, datetime

sessions_blueprint = Blueprint('sessions', __name__)

# Show all current sessions on system
@sessions_blueprint.route('/sessions')
def sessions():
    sessions = session_repository.select_all()
    return render_template('sessions/index.html', title='Training Sessions', sessions=sessions)

# Show an individual session
@sessions_blueprint.route('/sessions/<id>')
def show(id):
    session = session_repository.select(id)
    customers_booked = session_repository.customers(session)
    return render_template('sessions/show.html', title=session.name, session=session, customers_booked=customers_booked)

# Form to edit an individual session
@sessions_blueprint.route('/sessions/<id>/edit')
def edit(id):
    session = session_repository.select(id)
    today = date.today() #Grabs todays date so we can't set dates to be in the past
    return render_template('/sessions/edit.html', title=session.name, session=session, today=today)

# Update an individual session
@sessions_blueprint.route('/sessions/<id>', methods=['POST'])
def update_session(id):
    name = request.form['name']
    type = request.form['type']
    date_date = request.form['date']
    date = datetime.strptime(date_date, '%Y-%m-%d').strftime('%d-%m-%Y')
        # Date from the form is in reverse
        # This line reverses the date, as a string
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    capacity = request.form['capacity']
    updated_session = Session(name, type, date, start_time, end_time, capacity, id)

    if session_repository.availability_check(updated_session):
        session_repository.update(updated_session)
        return redirect('/sessions')
    else:
        return 'Session overlaps another'
   
# Form to add a new session
@sessions_blueprint.route('/sessions/new')
def new():
    today = date.today() #Grabs todays date so we can't set dates to be in the past
    return render_template('/sessions/new.html', title='New Training Session', today=today)

# #Create a new session
@sessions_blueprint.route('/sessions', methods=['POST'])
def create():
    name = request.form['name']
    type = request.form['type']
    date_date = request.form['date']
    date = datetime.strptime(date_date, '%Y-%m-%d').strftime('%d-%m-%Y')
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    capacity = request.form['capacity']
    new_session = Session(name, type, date, start_time, end_time, capacity)
    
    # Checks if there is an overlap with another session, assuming gym only has one room for sessions
    if session_repository.availability_check(new_session):
        session_repository.save(new_session)
        return redirect('/sessions')
    else:
        return 'Session overlaps another'

# Delete an individual session
@sessions_blueprint.route('/sessions/<id>/delete', methods=['POST'])
def delete(id):
    session_repository.delete(id)
    return redirect('/sessions')

