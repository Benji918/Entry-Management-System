import smtplib
import time
import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.urandom(20)
db = SQLAlchemy(app)
TWILIO_ACCOUNT_SID = 'ACaf7d96693d0ceb60b67bcfd752835c6d'
TWILIO_AUTH_TOKEN = '39520702d4b786b0a42eee4af7b33af0'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
MY_EMAIL = 'kodiugos@gmail.com'
PWD = 'llhytkakbfhnikci'


class host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    husername = db.Column(db.String(80))
    hemail = db.Column(db.String(120))
    userphone = db.Column(db.String(80))


class visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    visitorphone = db.Column(db.String(120))
    checkin = db.Column(db.String(120))


def host_send_email(visitor_name, visitor_emails, visitor_phones, visitor_checkins, host_email):
    text = "Hi Host,\n Visitor Name:\t" + visitor_name + "\n Visitor Email:\t" + visitor_emails + "\n Visitor Phone\t" + visitor_phones + "\n Checkin Time:\t" + visitor_checkins + "IST" + "\n visitor had just check in"
    subject = "Visitor has just checked in"
    message = 'Subject: {}\n\n{}'.format(subject, text)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Secure the connection
        connection.starttls()
        # login the user
        connection.login(user=MY_EMAIL, password=PWD)
        # send email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=host_email,
            msg=message
            .encode("utf-8")
        )


def visitor_send_email(visitor_name, visitor_email, visitor_phone, visitor_checkin, visitor_checkout, hostnames):
    # message to be sent 
    text = "Thank you Visitor for visiting us,\n Visitor Name:\t" + visitor_name + "\n Visitor Phone:\t" + visitor_phone + "\n Check-in Time:\t" + visitor_checkin + "IST" + "\n Check-out Time:\t" + visitor_checkout + "\n Host Name:\t" + hostnames + "\nAddress : Summergeeks by innovaccer"
    subject = "Thank you Visiting us"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Secure the connection
        connection.starttls()
        # login the user
        connection.login(user=MY_EMAIL, password=PWD)
        # send email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=visitor_email,
            msg=message
            .encode("utf-8")
        )


def sendSMS(message):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f'{message}',
        from_='+13253996972',
        to='+234 810 667 1579'
    )
    print(message.status)


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/host", methods=["GET", "POST"])
def hostpage():
    if request.method == "POST":
        hname = request.form['name']
        hemail = request.form['email']
        hphonenumber = request.form['phonenumber']

        if not hname:
            flash('Name cannot be empty!')
        elif not hemail:
            flash('Email cannot be empty!')
        elif not hphonenumber:
            flash('Phone number cannot be empty!')
        else:
            hregister = host(husername=hname, hemail=hemail, userphone=hphonenumber)
            db.session.add(hregister)
            db.session.commit()
            return redirect(url_for("hostthank"))
    return render_template("host.html")


@app.route("/hostthank", methods=["GET", "POST"])
def hostthank():
    return render_template("hostthank.html")


@app.route("/hostcheck")
def hostcheck():
    hrecords = host.query.order_by(host.id.desc()).first()

    host_email = hrecords.__dict__['hemail']
    host_phone = hrecords.__dict__['userphone']
    vrecord = visitor.query.order_by(visitor.id.desc()).first()
    visitor_names = vrecord.__dict__['username']
    visitor_emails = vrecord.__dict__['email']
    visitor_phones = vrecord.__dict__['visitorphone']
    visitor_checkins = vrecord.__dict__['checkin']
    host_send_email(visitor_names, visitor_emails, visitor_phones, visitor_checkins, host_email)
    sms_mes = "Name:" + " " + visitor_names + "\nEmail:" + visitor_emails + "\nPhone:" + visitor_phones + "\nCheckin:" + visitor_checkins
    sendSMS(message=sms_mes)
    return render_template("hostcheck.html")


@app.route("/visitoremail", methods=["GET", "POST"])
def visitoremail():
    if request.method == "POST":
        vrecords = visitor.query.order_by(visitor.id.desc()).first()

        visitor_name = vrecords.__dict__['username']
        visitor_email = vrecords.__dict__['email']
        visitor_phone = vrecords.__dict__['visitorphone']
        visitor_checkin = vrecords.__dict__['checkin']
        vt = time.localtime()
        visitor_checkout = time.strftime("%H:%M:%S", vt)
        hrecord = host.query.order_by(host.id.desc()).first()
        hostnames = hrecord.__dict__['husername']
        visitor_send_email(visitor_name, visitor_email, visitor_phone, visitor_checkin, visitor_checkout, hostnames)
        return render_template("thankvisitor.html")


@app.route("/visitorinfo", methods=["GET", "POST"])
def visitorinfo():
    if request.method == "POST":
        firstname = request.form['first-name']
        lastname = request.form['last-name']
        vname = firstname + " " + lastname
        visemail = request.form['vemail']
        visphone = request.form['vphone']
        vist = time.localtime()
        visitor_checkin = time.strftime("%H:%M:%S", vist)

        vregister = visitor(username=vname, email=visemail, visitorphone=visphone, checkin=visitor_checkin)
        db.session.add(vregister)
        db.session.commit()

        return redirect(url_for("hostcheck"))
    return render_template("visitor.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
