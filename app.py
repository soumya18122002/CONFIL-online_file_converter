from flask import Flask, render_template, redirect, request, url_for, session, flash, send_file
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime
import os
from werkzeug.utils import secure_filename
import jpgtopng
import jpgtopdf
import webptojpg
import pngtogif
import pngtosvg
import pngtotiff
import jpgtobmp
import jpgtojpeg
import pngtoico
import giftowbmp
import giftoeps
import jpgtoexr

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',
                      'tiff', 'csv', 'webp', 'wbmp', 'bmp', 'svg', 'ico', 'exr', 'eps'}
app = Flask(__name__)

app.secret_key = "Super Secret Key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
    return render_template('login.html', message=message, datetime=str(datetime.datetime.now()))


@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('Visitor_ID', None)
    session.pop('Email', None)
    return redirect(url_for('login'))


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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/jpgtopdf", methods=['POST', 'GET'])
def jpg_to_pdf():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = jpgtopdf.processimage_jpg_to_pdf(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('jpgtopdf.html')


@app.route("/jpgtopng", methods=['POST', 'GET'])
def jpg_to_png():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = jpgtopng.processimage_jpg_to_png(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('jpgtopng.html')


@app.route("/webptojpg", methods=['POST', 'GET'])
def webp_to_jpg():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = webptojpg.processimage_webp_to_jpg(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('webptojpg.html')


@app.route("/pngtogif", methods=['POST', 'GET'])
def png_to_gif():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = pngtogif.processimage_png_to_gif(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('pngtogif.html')


@app.route("/pngtosvg", methods=['POST', 'GET'])
def png_to_svg():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = pngtosvg.processimage_png_to_svg(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('pngtosvg.html')


@app.route("/pngtotiff", methods=['POST', 'GET'])
def png_to_tiff():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = pngtotiff.processimage_png_to_tiff(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('pngtotiff.html')


@app.route("/jpgtobmp", methods=['POST', 'GET'])
def jpg_to_bmp():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = jpgtobmp.processimage_jpg_to_bmp(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('jpgtobmp.html')


@app.route("/jpgtojpeg", methods=['POST', 'GET'])
def jpg_to_jpeg():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = jpgtojpeg.processimage_jpg_to_jpeg(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('jpgtojpeg.html')


@app.route("/pngtoico", methods=['POST', 'GET'])
def png_to_ico():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = pngtoico.processimage_png_to_ico(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('pngtoico.html')


@app.route("/giftowbmp", methods=['POST', 'GET'])
def gif_to_wbmp():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = giftowbmp.processiamage_gif_to_wbmp(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('giftowbmp.html')


@app.route("/giftoeps", methods=['POST', 'GET'])
def gif_to_eps():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = giftoeps.processiamage_gif_to_eps(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('giftoeps.html')


@app.route("/jpgtoexr", methods=['POST', 'GET'])
def jpg_to_exr():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            # return redirect(request.url)
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            return "No File Selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = jpgtoexr.processimage_jpg_to_exr(filename)
            print(fname)
            # msg = download_j_to_p()
            # print(msg)
            flash(
                f"Your image has been processed and is available <a href='/{fname}' target='_blank'>here</a>")
            # return redirect(url_for('download_file', name=filename))
            return send_file(fname, as_attachment=True)

            # return render_template('jpgtopng.html')
        # return "Post request is here"
    return render_template('jpgtoexr.html')

# @app.route("/download_j_to_p")
# def download_j_to_p():
#     return send_file(,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=80)
