from db.run_sql import run_sql

from models.session import Session
from models.customer import Customer

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


def select_by_id(id):
    session = None
    sql = 'SELECT * FROM sessions WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['name'], result['type'], result['date'], result['start_time'], result['end_time'], result['id'])
    return session


# This will be required if we want to display the customers booked into a given session
# def customers(session):
#     customers = []

#     sql = 'SELECT customers.* FROM customers INNER JOIN bookings ON bookings.customer_id = customers.id WHERE session_id = %s'
#     values = [session.id]
#     results = run_sql(sql, values)
#     for row in results:
#         customer = Customer(row['customer'], row['id'])
#         customers.append(customer)
#     return customers

def delete_all():
    sql = 'DELETE FROM sessions'
    run_sql(sql)

def delete_by_id(id):
    sql = 'DELETE FROM sessions WHERE id = %s'
    values = [id]
    run_sql(sql, values)
    # This currently isn't working in the browser

def update(session):
    sql = 'UPDATE sessions SET (name, type, date, start_time, end_time) = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [session.name, session.type, session.date, session.start_time, session.end_time]
    run_sql(sql,values)  