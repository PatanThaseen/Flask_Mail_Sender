from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'examplemail@gmail.com' #Replace with your mail
app.config['MAIL_PASSWORD'] = 'example_password'  # Replace with App Password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    email = request.form['email']
    message_content = request.form['message']
    
    msg = Message('Hello from Flask', sender='your-email@gmail.com', recipients=[email])
    msg.body = message_content
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
