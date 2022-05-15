from flask import Flask, Blueprint, render_template, request
from DAL import execute_sql, upd_sql,execute_sql_oneResult
from books import b_all

loans = Blueprint('loans',__name__,url_prefix='/loans')
 
@loans.route('/books/all/<CustomerID>/<BookID>/addLoan',methods=['GET', 'POST'])
def l_add(CustomerID,BookID):
    if request.method == 'GET':
    # CustomerID=request.args.get("CustomerID")
    # BookID=request.args.get("BookID")
        # sql=f"insert into Loans values (not null, {CustomerID},{BookID},{Published},{Type} )"
        return render_template("addLoan.html")
    else:
        LoanDate=request.form.get("LoanDate")
        sql=f"insert into Loans values (not null, {CustomerID},{BookID},{LoanDate}, "" )"
        print(sql)
        upd_sql(sql)
        sql="select * from Loans"
        loanList=execute_sql(sql)
        return render_template("loans.html",loanList=loanList)



   
 
# @books.route('/del/<id>')
# def b_del(id):
#     book=execute_sql_oneResult(f"select * from Books where BookID={id}")
#     upd_sql(f"delete from Books where BookID={id}")
#     return b_all(f"book {book[1]} was deleted!")
    
# @books.route('/all')
# def b_all(msg=""):
#     books=execute_sql("select * from Books")
#     context={
#         "books":books,
#         "msg":msg
#     }
#     print(execute_sql("select * from Books"))
#     return render_template('books.html', context=context)

# @books.route('/single/<id>')
# def b_single(id):
#     book=execute_sql_oneResult(f"select * from Books where BookID={id}")
#     return render_template("singleBook.html", book=book)

# @books.route('/single/<id>/upd',methods=['GET', 'POST'])
# def b_upd(id):
#     if request.method == 'GET':
#         book=execute_sql_oneResult(f"select * from Books where BookID={id}")
#         return render_template('updateBook.html', book=book)
#     else: #POST
#         Published=request.form.get('Published')
#         Type=request.form.get('Type')
#         sql=f"UPDATE Books SET Published={Published}, Type={Type} WHERE BookID={id}"
#         upd_sql(sql)
#         print(sql)
#         return b_all("Book is updated!")