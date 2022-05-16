from flask import Flask, Blueprint, render_template, request
from DAL import execute_sql, upd_sql,execute_sql_oneResult
from books import b_all
from datetime import datetime

loans = Blueprint('loans',__name__,url_prefix='/loans')
 
@loans.route('/<CustomerID>/<BookID>/addLoan',methods=['GET', 'POST'])
def l_add(CustomerID,BookID):
    if request.method == 'GET':
    # CustomerID=request.args.get("CustomerID")
    # BookID=request.args.get("BookID")
        # sql=f"insert into Loans values (not null, {CustomerID},{BookID},{Published},{Type} )"
        return render_template("addLoan.html")
    else:
        LoanDate=request.form.get("LoanDate")
        sql=f'''insert into Loans values (not null, '{CustomerID}','{BookID}','{LoanDate}', "{" "}" )'''
        print(sql)
        upd_sql(sql)
        return l_all()

@loans.route('/all')
def l_all():
    loanlist=execute_sql("SELECT LoanID, Customers.customerName,Books.bookName,Books.Type,LoanDate,ReturnDate FROM Loans \
        INNER JOIN Customers ON Loans.CustomerID=Customers.CustomerID INNER JOIN Books ON Loans.BookID=Books.BookID")
    return render_template("loans.html", loanlist=loanlist)

@loans.route('/<LoanID>/all/returnLoan',methods=['GET', 'POST'])
def l_return(LoanID):
    if request.method == 'GET':
        return render_template("returnLoan.html")
    else:
        ReturnDate=request.form.get("ReturnDate")
        sql=f'''select LoanDate from Loans where LoanID={LoanID}'''
        compare=execute_sql_oneResult(sql)
        if compare[0]>ReturnDate:
            # upd_sql(f'''update Loans SET ReturnDate="{" "}" where LoanID={LoanID}''')
            msg="Enter valid return date"
            return render_template("returnLoan.html",msg=msg)
        else:
            sql=f"UPDATE Loans SET ReturnDate='{ReturnDate}' WHERE LoanID={LoanID}"
            upd_sql(sql)
            return l_all()

@loans.route('/<LoanID>/all/status')
def loanStatus(LoanID):
    checkType=execute_sql_oneResult(f"SELECT LoanDate,ReturnDate,Type FROM Loans INNER JOIN Books ON Loans.BookID=Books.BookID WHERE LoanID={LoanID}")
    if checkType[1]==" ":
        msg="Not Returned"
        msg2="0"
        return render_template("status.html",msg=msg,msg2=msg2)
    else:
        for n in checkType:
                print(checkType[2])
                if checkType[2]==1:
                    date_format = "%Y-%m-%d"
                    loanDate = datetime.strptime(checkType[0], date_format)
                    returnDate = datetime.strptime(checkType[1], date_format)
                    delta = returnDate-loanDate
                    myDif=delta.days
                    if myDif>10:
                        overDays=myDif-10
                        msg="returned"
                        return render_template("status.html",overDays=overDays,msg=msg)
                if checkType[2]==2:
                    date_format = "%Y-%m-%d"
                    loanDate = datetime.strptime(checkType[0], date_format)
                    returnDate = datetime.strptime(checkType[1], date_format)
                    delta = returnDate-loanDate
                    myDif=delta.days
                    if myDif>5:
                        overDays=myDif-5
                        msg="returned"
                        return render_template("status.html",overDays=overDays,msg=msg)
                if checkType[2]==3:
                    date_format = "%Y-%m-%d"
                    loanDate = datetime.strptime(checkType[0], date_format)
                    returnDate = datetime.strptime(checkType[1], date_format)
                    delta = returnDate-loanDate
                    myDif=delta.days
                    if myDif>2:
                        overDays=myDif-2
                        msg="returned"
                        return render_template("status.html",overDays=overDays,msg=msg)
                    
