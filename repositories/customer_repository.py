from db.run_sql import run_sql

from models.customer import Customer
from models.session import Session

def save(customer):
    sql = 'INSERT INTO customers( forename, surname, alias, membership_status, membership_type ) VALUES ( %s, %s, %s, %s, %s) RETURNING id'
    values = [customer.forename, customer.surname, customer.alias, customer.membership_status, customer.membership_type]
    results = run_sql( sql, values)
    customer.id = results[0]['id']
    return customer

def select_all():
    customers = []
    sql = 'SELECT * FROM customers'
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['forename'], row['surname'], row['alias'], row['membership_status'], row['membership_type'],row['id'])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql = 'SELECT * FROM customers WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        customer = Customer(result['forename'], result['surname'], result['alias'], result['membership_status'], result['membership_type'],result['id'])
    return customer

def update(customer):
    sql = 'UPDATE customers SET (forename, surname, alias, membership_status, membership_type) = row(%s, %s, %s, %s, %s) WHERE id = %s'
    # This is a weird one. Session didn't need row(%s) to work, just (%s)
    # Is it because I only have the one variable?
    # See what happens when I add in extensions
    values = [customer.forename, customer.surname, customer.alias, customer.membership_status, customer.membership_type, customer.id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM customers'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM customers WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# This will be required if we want to display session bookings for a given customer:
def sessions(customer):
    sessions = []
    sql = 'SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE customer_id = %s'
    values = [customer.id]
    results = run_sql(sql, values)
    for row in results:
        session = Session(row['name'], row['type'], row['date'], row['start_time'], row['end_time'])
        sessions.append(session)
    return sessions

def duplicate_check(new_customer):
    customers = select_all()
    for customer in customers:
        if customer.alias == new_customer.alias: 
            return True
    return False
