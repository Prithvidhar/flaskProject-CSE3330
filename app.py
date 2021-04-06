from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prithvidhar'

mysql = MySQL(app)


@app.route('/')
def root():
    return render_template('index.html')
@app.route('/fetchdata', methods=['GET', 'POST'])
def display():
    if request.method == "POST":
        details = request.form
        design = details['Designation']
        em = details['email']
        phone = details['phoneNo']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM officials AS O WHERE O.Designation = '" + design + "' AND O.Email = '" + em + "' AND O.Phone_No = '" + phone + "'")
        result = cur.fetchall()
        print(result)
        mysql.connection.commit()
        cur.close()
        return render_template('theQuery.html', result = result)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        details = request.form
        id = details['idText']
        name = details['nameText']
        job = details['jobText']
        email = details['emailText']
        phone = details['phoneText']

        cur = mysql.connection.cursor()
        cur.execute("INSERT into officials VALUES (%s, %s, %s, %s, %s, %s)", (id, "TX", name, job, email, phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
