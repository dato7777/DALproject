import sqlite3
con = sqlite3.connect('Library.db', check_same_thread=False)

cur = con.cursor()

# Create table
def initDB():
    try:
        cur.execute('''CREATE TABLE Books (BookID INTEGER PRIMARY KEY, bookName text, Author text, Published int, Type int)''')
    except:pass
    try:
        cur.execute('''CREATE TABLE Customers (CustomerID INTEGER PRIMARY KEY, customerName text, City text, Age int)''')
    except:pass
    try:
        cur.execute('''CREATE TABLE Loans (LoanID INTEGER PRIMARY KEY, CustomerID INTEGER NOT NULL, BookID INTEGER NOT NULL, LoanDate int, ReturnDate int,
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID), FOREIGN KEY (BookID) REFERENCES Books (BookID))''')
    except:pass

    customers_list = [
         (('Jacob Gor'),('Bat Yam'),(42)),
         (('Sam Franklin'),('London'),(23)),
         (('Natasha Zeiss'),('Antwerpen'),(18)),
         (('Omer Sasson'),('Tel Aviv'),(30)),
         (('Michael Bradley'),('Bat Yam'),(42)),
         (('Avner Ivanov'),('Kiev'),(20)),
         (('Giorgi Kinkladze'),('Tbilisi'),(17))]

    book_list = [
        (('Carrie'),('Stephen King'),(1974),(1)),
        (('The Godfather'),('Mario Puzo'),(1969),(3)),
        (('Babbitt'),('Sinclair Lewis'),(1922), (2)),
        (('Money'),('Martin Amis'),(1984), (3)),
        (('Midnights Children'),('Salman Rushdie'),(1981), (1)),
        (('East of Eden'),('John Steinbeck'),(1952), (2)),
        (('Foundation'),('Isaac Asimov'),(1942), (3))]
    
    cur.executemany("insert into Customers ('customerName', 'City', 'Age') values (?,?,?)", (customers_list)) 
    cur.executemany("insert into Books ('bookName','Author','Published','Type') values(?,?,?,?)", (book_list))
    con.commit()
    for row in cur.execute('SELECT DISTINCT * FROM Books'):
        print(row)

def execute_sql(sql):
    return cur.execute(sql).fetchall()

def execute_sql_oneResult(sql):
    return cur.execute(sql).fetchone()

def upd_sql(sql):
    cur.execute(sql)
    con.commit()

    
# # Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# con.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# con.close()