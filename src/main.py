from flask import Flask, redirect, render_template, request, abort
import socket
from User import User
from simple_salesforce import Salesforce


app = Flask(__name__)
sf = Salesforce(username='fouronf@curious-impala-l5jd5q.com', password='Bibou23-', security_token='OL8PmqjNwRkPyuYFQF9CNLi2')

class Session:
    """ This object will be the bridge between the Salesforce API and the local instance of the running application """
    def __init__(self) -> None:
        self.user = None
        self.task_list = []
        self.non_blocked = []

    def set_user(self, user: User):
        self.user = user

    def get_username(self):
        return self.username
    
    def check_credentials(self):
        ### check credentials using api calls using the SalesForce object ###
        pass

    def get_non_blocked_ips(self):
        return self.non_blocked
    

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

@app.route('/welcome', methods=["GET", "POST"])
def welcome():
    if request.method == 'POST':
        username = request.form['username']
        user_password = request.form['password']
        return username, user_password
    return render_template("welcome.html")

#access api to check credentials#

user1 = User("fouronf", "Fabrice", "Fouron", "fouronf@wit.edu")

@app.route('/todo')
def todo_list():
    return render_template("todo.html", task_list=[user1])

#############################################
if __name__ == '__main__':
    app.run(debug=True)
