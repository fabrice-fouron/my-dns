from flask import Flask, redirect, render_template, request, abort
import socket
from User import User
from simple_salesforce import Salesforce


app = Flask(__name__)
sf = Salesforce(username='fouronf@curious-impala-l5jd5q.com', password='Bibou23-', security_token='OL8PmqjNwRkPyuYFQF9CNLi2')

class Session:
    def __init__(self) -> None:
        self.user = None

    def set_user(self, user: User):
        self.user = user


non_blocked = ["127.0.0.1"] # IP addresses that are not blocked

def get_ip_address(url: str) -> str:
    """ Gets the IP address of a given url """
    ip_address = socket.gethostbyname(url)
    return ip_address

def add_ips(ip: str) -> None:
    """ Adds a given ip address in the non_blocked list """
    non_blocked.append(ip)

##################################################

    

##################################################



# methods regarding the flask application for generating pages and handling them
#############################################
@app.before_request
def block_ip():
    client_ip = request.remote_addr
    if client_ip not in non_blocked:
        abort(403)  # Return forbidden status code if IP is blocked


@app.route("/")
def empty():
    return render_template("index.html")

@app.route('/placeholder')
def placeholder():
    return "<h1>Placeholder</h1>"

@app.route('/welcome', methods=["POST"])
def welcome():
    if request.method == 'POST':
        username = request.form['username']
        userPassword = request.form['password']
        return userEmail, userPassword
    return render_template("welcome.html")

#access api to check credentials#

user1 = User("fouronf", "Fabrice", "Fouron", "fouronf@wit.edu")
user2 = User("fabricefouron", 'fabrice', 'fouron', 'fabricefouron@gmail.com')

@app.route('/todo')
def todo_list():
    return render_template("todo.html", task_list=[user1, user2])

#############################################
if __name__ == '__main__':
    app.run(debug=True)
