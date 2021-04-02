from db.run_sql import run_sql

from models.session import Session

def save(session):
    sql = 'INSERT INTO sessions( name, type, date, start_time, end_time ) VALUES ( %s, %s, %s, %s, %s ) RETURNING id'
    values = [session.name, session.type, session.date, session.start_time, session.end_time]
    results = run_sql( sql, values)
    session.id = results[0]['id']
    return session


def select_all():
    sessions = []
    sql = 'SELECT * FROM sessions'
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['type'], row['date'], row['start_time'], row['end_time'], row['id'])
        sessions.append(session)
    return sessions


def select(id):
    session = None
    sql = 'SELECT * FROM sessions WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['name'], result['type'], result['date'], result['start_time'], result['end_time'], result['id'])
        # Add in extensions here when required
    return session

def delete_all():
    sql = 'DELETE FROM sessions'
    run_sql(sql)