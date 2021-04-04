from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint('sessions', __name__)

# Show all current sessions on system
@sessions_blueprint.route('/sessions')
def sessions():
    sessions = session_repository.select_all()
    return render_template('sessions/index.html', sessions=sessions)

# Show an individual session
@sessions_blueprint.route('/sessions/<id>')
def show(id):
    session = session_repository.select(id)
    customers_booked = session_repository.customers(session)
    return render_template('sessions/show.html', session=session, customers_booked=customers_booked)

# Form to edit an individual session
@sessions_blueprint.route('/sessions/<id>/edit')
def edit(id):
    session = session_repository.select(id)
    return render_template('/sessions/edit.html', session=session)

# Update an individual session
@sessions_blueprint.route('/sessions/<id>', methods=['POST'])
def update_session(id):
    name = request.form['name']
    type = request.form['type']
    date = request.form['date']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    session = Session(name, type, date, start_time, end_time, id)
    session_repository.update(session)
    return redirect('/sessions')

# Form to add a new session
@sessions_blueprint.route('/sessions/new')
def new():
    return render_template('/sessions/new.html')

# #Create a new session
@sessions_blueprint.route('/sessions', methods=['POST'])
def create():
    name = request.form['name']
    type = request.form['type']
    date = request.form['date']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    session = Session(name, type, date, start_time, end_time)
    session_repository.save(session)
    return redirect('/sessions')

# Delete an individual session
@sessions_blueprint.route('/sessions/<id>/delete', methods=['POST'])
def delete(id):
    session_repository.delete(id)
    return redirect('/sessions')

