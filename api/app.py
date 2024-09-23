from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Usando variável de ambiente
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Usando variável de ambiente

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=["POST"])
def send_email():
    nome = request.form['nome']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    msg = Message(subject=subject, sender=email, recipients=[os.environ.get('MAIL_USERNAME')])
    msg.body = message
    mail.send(msg)

    return render_template('email_sent.html')  # Renderizando a página de confirmação

if __name__ == '__main__':
    app.run(debug=True)



