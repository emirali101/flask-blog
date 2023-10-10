from flask import Flask, render_template, request
import requests
import smtplib

#OWN_EMAIL = email_adress
#OWN_PASSWORD = email_password

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(url="https://api.npoint.io/d19a0960cf2c9f772219")
    all_post = response.json()
    return render_template("index.html", posts=all_post)


@app.route("/about.html/")
def about_page():
    return render_template("about.html")


@app.route("/contact.html/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html", message_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/post/<int:blog_id>.html")
def go_read(blog_id):
    response = requests.get(url="https://api.npoint.io/d19a0960cf2c9f772219")
    all_post = response.json()
    post = all_post[blog_id - 1]
    return render_template("post.html", post=post)


if __name__=="__main__":
    app.run()

