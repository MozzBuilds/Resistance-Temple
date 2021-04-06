from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint('customers', __name__)

# Show all customers
@customers_blueprint.route('/customers')
def customers():
    customers = customer_repository.select_all()
    return render_template('customers/index.html', title='Customers', customers = customers)

# Show a customer
@customers_blueprint.route('/customers/<id>')
def show(id):
    customer = customer_repository.select(id)
    sessions_booked = customer_repository.sessions(customer)
    return render_template('customers/show.html', title=customer.alias, customer=customer, sessions_booked=sessions_booked)

# Form to edit a customer
@customers_blueprint.route('/customers/<id>/edit')
def edit(id):
    customer = customer_repository.select(id)
    membership_types = customer.membership_types # A list of possible membership types
    membership_status_types = customer.membership_status_types # A list of possible membership status types
    return render_template('/customers/edit.html', title=customer.alias, customer=customer, membership_types=membership_types, membership_status_types=membership_status_types)

# Updating the customer with the edited data
@customers_blueprint.route('/customers/<id>', methods=['POST'])
def update_customer(id):
    customer = customer_repository.select(id) #Grabs the customers current information
    customer_alias = customer.alias #Grabs the customers current, fixed alias which cannot be changed
    forename = request.form['forename']
    surname = request.form['surname']
    membership_status = request.form['membership_status']
    membership_type = request.form['membership_type']
    updated_customer = Customer(forename, surname, customer_alias, membership_status, membership_type,id)
    customer_repository.update(updated_customer)
    return redirect('/customers')

# Form to add a new customer
@customers_blueprint.route('/customers/new')
def new():
    return render_template('/customers/new.html', title='New Customer')

#Create a new customer
@customers_blueprint.route('/customers', methods=['POST'])
def create():
    forename = request.form['forename']
    surname = request.form['surname']
    alias = request.form['alias']
    membership_status = request.form['membership_status']
    membership_type = request.form['membership_type']
    new_customer = Customer(forename, surname, alias, membership_status, membership_type)
    if customer_repository.duplicate_check(new_customer):
        return 'That alias has already been taken. The customer may choose another, or the customer may already be on the system'
    else:
        customer_repository.save(new_customer)
        return redirect('/customers')

# Delete a customer
@customers_blueprint.route('/customers/<id>/delete', methods=['POST'])
def delete(id):
    customer_repository.delete(id)
    return redirect ('/customers')