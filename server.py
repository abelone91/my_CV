from flask import Flask, render_template, url_for, request
import csv
#render template to use own html, CCS and js
app = Flask(__name__)

@app.route('/')
def my_web():
    return render_template('index.html')
#----------------------------------------------------
#sending email via contact form

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        write_to_csv(name, email, subject, message) #can also use write to file for txt format
        return 'Thank you for getting in contact. I will reach out to you shortly.'
    else:
        return 'something went wrong'

def write_to_file(name, email, subject, message):
    with open('database.txt', mode ='a') as database:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        file = database.write(f'\n {name}, {email}, {subject}, {message}')

def write_to_csv(name, email, subject, message):
    with open('database.csv', newline='', mode ='a') as database2:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])