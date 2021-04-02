from db.run_sql import run_sql

from models.customer import Customer
from models.session import Session

def save(customer):
    sql = 'INSERT INTO customers( name ) VALUES ( %s ) RETURNING id'
    # Add in extensions here when required
    values = [customer.name]
    results = run_sql( sql, values)
    customer.id = results[0]['id']
    return customer

def select_all():
    customers = []
    sql = 'SELECT * FROM customers'
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['name'], row['id'])
        # Add in extensions here when required
        customers.append(customer)
    return customers

def select_by_id(id):
    customer = None
    sql = 'SELECT * FROM customers WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        customer = Customer(result['name'], result['id'])
        # Add in extensions here when required
    return customer

# This will be required if we want to display session bookings for a given customer:
# def sessions(customer):
#     sessions = []
#     sql = 'SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE customer_id = %s'
#     values = [customer.id]
#     results = run_sql(sql, values)
#     for row in results:
#         session = Session(row['name'], row['type'], row['date'], row['start_time'], row['end_time'])
#         sessions.append(session)
#     return sessions

def delete_all():
    sql = 'DELETE FROM customers'
    run_sql(sql)

def delete_by_id(id):
    sql = 'DELETE FROM customers WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(customer):
    sql = 'UPDATE customers SET (name) = (%s) WHERE id = %s'
    values = [customer.name]
    run_sql(sql,values)