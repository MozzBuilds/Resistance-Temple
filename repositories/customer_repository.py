from db.run_sql import run_sql

from models.customer import Customer
from models.session import Session

# Saves a customer
def save(customer):
    sql = 'INSERT INTO customers( forename, surname, alias, membership_status, membership_type ) VALUES ( %s, %s, %s, %s, %s) RETURNING id'
    values = [customer.forename, customer.surname, customer.alias, customer.membership_status, customer.membership_type]
    results = run_sql( sql, values)
    customer.id = results[0]['id']
    return customer

# Selects all customers
def select_all():
    customers = []
    sql = 'SELECT * FROM customers'
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['forename'], row['surname'], row['alias'], row['membership_status'], row['membership_type'],row['id'])
        customers.append(customer)
    return customers

# Selects an individual customer
def select(id):
    customer = None
    sql = 'SELECT * FROM customers WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        customer = Customer(result['forename'], result['surname'], result['alias'], result['membership_status'], result['membership_type'],result['id'])
    return customer

# Updates a customers details
def update(customer):
    sql = 'UPDATE customers SET (forename, surname, alias, membership_status, membership_type) = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [customer.forename, customer.surname, customer.alias, customer.membership_status, customer.membership_type, customer.id]
    run_sql(sql,values)

# Deletes all customers - Only used by console.py currently
def delete_all():
    sql = 'DELETE FROM customers'
    run_sql(sql)

# Deletes a customer
def delete(id):
    sql = 'DELETE FROM customers WHERE id = %s'
    values = [id]
    run_sql(sql, values)

# For displaying sessions booked on the Customer show page
def sessions(customer):
    sessions = []
    sql = 'SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE customer_id = %s'
    values = [customer.id]
    results = run_sql(sql, values)
    for row in results:
        session = Session(row['name'], row['type'], row['date'], row['start_time'], row['end_time'], row['capacity'])
        sessions.append(session)
    return sessions

# Returns True if there is a duplicate alias found
def duplicate_check(new_customer):
    customers = select_all()
    for customer in customers:
        if customer.alias == new_customer.alias: 
            return True
    return False

# Returns True if the customer membership status is active
def membership_status_check(customer_id):
    customer = select(customer_id)
    if customer.membership_status == 'Active':
        return True
    else:
        return False