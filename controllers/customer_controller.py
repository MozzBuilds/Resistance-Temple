from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint('customers', __name__)

# Show all customers
@customers_blueprint.route('/customers')
def customers():
    customers = customer_repository.select_all()
    return render_template('customers/index.html', customers = customers)

# Show a customer
@customers_blueprint.route('/customers/<id>')
def show(id):
    customer = customer_repository.select(id)
    return render_template('customers/show.html', customer=customer)

# Form to edit a customer
@customers_blueprint.route('/customers/<id>/edit')
def edit(id):
    customer = customer_repository.select(id)
    return render_template('/customers/edit.html', customer=customer)

# Updating the customer with the edited data
@customers_blueprint.route('/customers/<id>', methods=['POST'])
def update_customer(id):
    name = request.form['name']
    customer = Customer(name, id)
    customer_repository.update(customer)
    return redirect('/customers')
    # All this is currently doing is redirecting back to /customers
    # Terminal error:
        # source for a multiple-column UPDATE item must be a sub-SELECT or ROW() expression
        # LINE 1: UPDATE customers SET (name) = ('Morpheuss') WHERE id = '4'

# Form to add a new customer
@customers_blueprint.route('/customers/new')
def new():
    return render_template('/customers/new.html')

#Create a new customer
@customers_blueprint.route('/customers', methods=['POST'])
def create():
    name = request.form['name']
    customer = Customer(name)
    customer_repository.save(customer)
    return redirect('/customers')

# Delete a customer
@customers_blueprint.route('/customers/<id>/delete', methods=['POST'])
def delete(id):
    customer_repository.delete(id)
    return redirect ('/customers')