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
    membership_types = customer.membership_types # A list of possible membership types
    membership_status_types = customer.membership_status_types # A list of possible membership status types
    return render_template('/customers/edit.html', customer=customer, membership_types=membership_types, membership_status_types=membership_status_types)

# Updating the customer with the edited data
@customers_blueprint.route('/customers/<id>', methods=['POST'])
def update_customer(id):
    forename = request.form['forename']
    surname = request.form['surname']
    alias = request.form['alias']
    membership_status = request.form['membership_status']
    membership_type = request.form['membership_type']
    customer = Customer(forename, surname, alias, membership_status, membership_type,id)
    customer_repository.update(customer)
    return redirect('/customers')

# Form to add a new customer
@customers_blueprint.route('/customers/new')
def new():
    return render_template('/customers/new.html')

#Create a new customer
@customers_blueprint.route('/customers', methods=['POST'])
def create():
    forename = request.form['forename']
    surname = request.form['surname']
    alias = request.form['alias']
    membership_status = request.form['membership_status']
    membership_type = request.form['membership_type']
    new_customer = Customer(forename, surname, alias, membership_status, membership_type)
    if customer_repository.duplicate_check(new_customer) == True:
        return 'That alias has already been taken. The customer may choose another, or the customer may already be on the system'
    else:
        customer_repository.save(new_customer)
        return redirect('/customers')
    customer_repository.save(new_customer)
    return redirect('/customers')

# Delete a customer
@customers_blueprint.route('/customers/<id>/delete', methods=['POST'])
def delete(id):
    customer_repository.delete(id)
    return redirect ('/customers')