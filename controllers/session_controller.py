from flask import Flask, render_template
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint('sessions', __name__)

@sessions_blueprint.route('/sessions')
def sessions():
    sessions = session_repository.select_all()
    return render_template('sessions/index.html', sessions=sessions)

@sessions_blueprint.route('/sessions/<id>')
def show(id):
    session = session_repository.select_by_id(id)
    return render_template('sessions/show.html', session=session)