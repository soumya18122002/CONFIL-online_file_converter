from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime

app = Flask(__name__)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/file_upload")
def file_upload():
    return render_template("file_upload.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/twitter")
def twitter():
    return redirect("https://twitter.com")


@app.route("/linkedin")
def linkedin():
    return redirect("https://linkedin.com")


@app.route("/facebook")
def facebook():
    return redirect("https://facebook.com")


@app.route("/instagram")
def instagram():
    return redirect("https://instagram.com")


@app.route("/github")
def github():
    return redirect("https://github.com")


@app.route("/snapchat")
def snapchat():
    return redirect("https://snapchat.com")


app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'YTXr@295'
app.config['MYSQL_DB'] = 'confil_register'

mysql = MySQL(app)


@app.route("/", methods=['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST' and 'eml_add' in request.form and 'passw' in request.form:
        eml_add = request.form.get('eml_add')
        passw = request.form.get('passw')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM visitor_details WHERE Email = %s AND Passwords = %s', (eml_add, passw, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['Visitor_ID'] = user['Visitor_ID']
            session['Visitor_Name'] = user['Visitor_Name']
            session['Email'] = user['Email']
            message = 'Logged in Succesfully!!'
            return redirect(url_for('dashboard'))
        else:
            message = 'Please enter the correct email / password !!'
    return render_template('login.html', message=message)


@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('Visitor_ID', None)
    session.pop('Email', None)
    return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'eml' in request.form and 'psw' in request.form and 'con_psw' in request.form and 'phon' in request.form and 'dob' in request.form and 'gender' in request.form and 'st_add1' in request.form and 'st_add2' in request.form and 'ctry' in request.form and 'cit' in request.form and 'reg' in request.form and 'pcode' in request.form:
        name = request.form.get('name')
        eml = request.form.get('eml')
        psw = request.form.get('psw')
        con_psw = request.form.get('con_psw')
        phon = request.form.get('phon')
        dob = datetime.datetime.strptime(request.form['dob'], '%Y-%m-%d')
        gender = request.form.get('gender')
        st_add1 = request.form.get("st_add1")
        st_add2 = request.form.get("st_add2")
        ctry = request.form.get("ctry")
        cit = request.form.get("cit")
        reg = request.form.get("reg")
        pcode = request.form.get("pcode")
        # return f"your all details are{name},{eml},{psw},{con_psw},{phon},{dob},{gender},{st_add1},{st_add2},{ctry},{cit},{reg},{pcode}"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM visitor_details WHERE Email=%s', (eml, ))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists!!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]', eml):
            message = 'Invalid email address!!'
        elif not 'name' or not 'eml' or not 'psw' or not 'con_psw' or not 'phon' or not 'dob' or not 'gender' or not 'st_add1' or not 'st_add2' or not 'ctry' or not 'cit' or not 'reg' or not 'pcode':
            message = 'Please fill out the Form!!'
        else:
            cursor.execute('INSERT INTO visitor_details VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           (name, eml, psw, con_psw, phon, dob, gender, st_add1, st_add2, ctry, cit, reg, pcode, ))
            mysql.connection.commit()
            message = 'You have successfully registered!!'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        message = 'Please fill out the Form!!'
    return render_template('register.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
