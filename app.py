from flask import Flask, render_template, Blueprint
from DAL import initDB
from customers import customers
from books import books
from loans import loans
api = Flask(__name__)
api.register_blueprint(customers)
api.register_blueprint(books)
api.register_blueprint(loans)

# initDB()
 
@api.route('/')
def hello():
    return render_template('index.html')

@api.route('/test')
def test():
    return render_template('customers.html')
 
 
if __name__ == '__main__':
    api.run(debug=True)