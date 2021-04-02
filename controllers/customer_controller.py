from flask import Flask, render_template
from flask import Blueprint
from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint('customers', __name__)

@customers_blueprint.route('/customers')
def customers():
    customers = customer_repository.select_all()
    return render_template('customers/index.html', customers = customers)
