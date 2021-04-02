from flask import Flask, render_template

from controllers.booking_controller import bookings_blueprint
from controllers.session_controller import sessions_blueprint
from controllers.customer_controller import customers_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(customers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)