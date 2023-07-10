from flask import Flask
from flask import request,jsonify
from demo import register_db,bicycle_db,login_db,transaction_db
from flask_cors import CORS
import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv  # pip install python-dotenv


app = Flask(__name__)
CORS(app)

@app.route('/',methods = ['get'])
def test():
    return 'hello'

@app.route('/register',methods = ['post'])
def register():
    req = request.get_json()
    print(req)
    res = register_db(req)
    return jsonify(res)


@app.route('/bicycle', methods=['get'])
def bicycle():
    res = bicycle_db()
    return jsonify(res)


@app.route('/login',methods = ['post'])
def login():
    req = request.get_json()
    print(req)
    res = login_db(req)
    return jsonify(res)


@app.route('/transaction',methods = ['post'])
def transaction():
    req = request.get_json()
    print(req)
    res = transaction_db(req)
    return jsonify(res)


@app.route('/gettransaction',methods = ['get'])
def get_transaction():
    res = gettransaction_db()
    return jsonify(res)

@app.route('/etl_bicycles',methods = ['get'])
def etl_bicycles():
    res = etlbicycles_db()
    return jsonify(res)
   

PORT = 587  
EMAIL_SERVER = "smtp.googlemail.com"  # Adjust server address, if you are not using @outlook

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name, bike_make_model):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Bworks Org.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I hope you are well.
        I just wanted to drop you a quick note to thank you for the donation of {bike_make_model} to our organisation.
        The childern of Bworks community are really grateful for your kind thoughts and actions.

        Best regards
        Patrick
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to thank you for the donation of <strong>{bike_make_model}</strong> to our organisation..</p>
        <p>The childern of Bworks community are really grateful for your kind thoughts and actions.</p>
        <p>Best regards</p>
        <p>Patrick</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Thank you Mail",
        receiver_email="akhilvemulapally@gmail.com",
        name="Akhil",
        bike_make_model = "Trek 520",
    )
    app.run()
