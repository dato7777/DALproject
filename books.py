from flask import Flask, Blueprint, render_template, request
from DAL import execute_sql, upd_sql,execute_sql_oneResult

books = Blueprint('books',__name__,url_prefix='/books')
 
@books.route('/add',methods=['GET', 'POST'])
def b_add():
    if request.method == 'GET':
        return render_template('addBook.html')
    else: #POST
        name=request.form.get('bookName')
        Author=request.form.get('Author')
        Published=request.form.get('Published')
        Type=request.form.get('Type')
        sql=f"insert into Books values (not null, '{name}','{Author}',{Published},{Type} )"
        upd_sql(sql)
        return b_all("Book was added!")
 
@books.route('/del/<id>')
def b_del(id):
    book=execute_sql_oneResult(f"select * from Books where BookID={id}")
    upd_sql(f"delete from Books where BookID={id}")
    return b_all(f"book {book[1]} was deleted!")

@books.route('/all/<id>')   
@books.route('/all')
def b_all(id=-1, msg=""):
    books=execute_sql("select * from Books")
    context={
        "books":books,
        "msg":msg,
        "id":id
    }
    
    return render_template('books.html', context=context)

@books.route('/single/<id>')
def b_single(id):
    book=execute_sql_oneResult(f"select * from Books where BookID={id}")
    return render_template("singleBook.html", book=book)

@books.route('/single/<id>/upd',methods=['GET', 'POST'])
def b_upd(id):
    if request.method == 'GET':
        book=execute_sql_oneResult(f"select * from Books where BookID={id}")
        return render_template('updateBook.html', book=book)
    else: #POST
        Published=request.form.get('Published')
        Type=request.form.get('Type')
        sql=f"UPDATE Books SET Published={Published}, Type={Type} WHERE BookID={id}"
        upd_sql(sql)
        
        return b_all("Book is updated!")