from flask import Flask, render_template, request, url_for, redirect
# email stuff below! 
from email.mime.text import MIMEText 
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# route to index.html
@app.route("/") 
def index():
    return render_template("index.html")

#Create a route that loads when the user clicks the SUbmit button (send) on the email form - sending data via POST method
@app.route("/sendemail/", methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        #Set your credentials (note: security here , do not upload your passwords to GitHub lol)

yourEmail = 
yourPassword = 