from crypt import methods
from flask import Flask, Blueprint, render_template, request

from DAL import execute_sql, upd_sql,execute_sql_oneResult

customers = Blueprint('customers',__name__,url_prefix='/customers')
 
@customers.route('/add',methods=['GET', 'POST'])
def c_add():
    if request.method == 'GET':
        return render_template('addCustomer.html')
    else: #POST
        name=request.form.get('customerName')
        city=request.form.get('City')
        age=request.form.get('Age')
        sql=f"insert into Customers values (not null, '{name}','{city}',{age})"
        upd_sql(sql)
        return c_all("customer was added!")
 
@customers.route('/del/<id>')
def c_del(id):
    customer=execute_sql_oneResult(f"select * from Customers where CustomerID={id}")
    upd_sql(f"delete from Customers where CustomerID={id}")
    return c_all(f"customer {customer[1]} was deleted!")

@customers.route('/all')
def c_all(msg=""):
    customers=execute_sql("select * from Customers")
    context={
        "customers":customers,
        "msg":msg
    }
    return render_template('customers.html', context=context)

@customers.route('/single/<id>')
def c_single(id):
    customer=execute_sql_oneResult(f"select * from Customers where CustomerID={id}")
    return render_template("singleCustomer.html", customer=customer)

@customers.route('/single/<id>/upd',methods=['GET', 'POST'])
def c_upd(id):
    if request.method == 'GET':
        customer=execute_sql_oneResult(f"select * from Customers where CustomerID={id}")
        return render_template('updateCustomer.html', customer=customer)
    else: #POST
        city=request.form.get('City')
        age=request.form.get('Age')
        sql=f"UPDATE Customers SET City='{city}', Age='{age}' WHERE CustomerID={id}"
        upd_sql(sql)
        
        return c_all("customer is updated!")
    