from db.run_sql import run_sql

from models.customer import Customer

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

def delete_all():
    sql = 'DELETE FROM customers'
    run_sql(sql)