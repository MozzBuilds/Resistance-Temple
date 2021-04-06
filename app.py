from flask import Flask, render_template

from controllers.bookings_controller import bookings_blueprint
from controllers.sessions_controller import sessions_blueprint
from controllers.customers_controller import customers_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(customers_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/info')
def other():
    return render_template('info/index.html', title='Info')

if __name__ == '__main__':
    app.run(debug=True)



