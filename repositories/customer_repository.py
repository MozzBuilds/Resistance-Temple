from db.run_sql import run_sql

from models.customer import Customer

def select_all():
    customers = []
    sql = 'SELECT * FROM customers'
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['name'], row['id'])
        customers.append(customer)
    return customers