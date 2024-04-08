from flask import Flask, redirect, render_template, request, abort
import socket
from User import User
from simple_salesforce import Salesforce
from util import *
from datetime import datetime


app = Flask(__name__)
sf = Salesforce(username='fouronf@curious-impala-l5jd5q.com', password='Bibou23-', security_token='OL8PmqjNwRkPyuYFQF9CNLi2')
session = None

class Session:
    """ This object will be the bridge between the Salesforce API and the local instance of the running application """
    """Assumption: you can have 1 task per timeframe"""
    def __init__(self) -> None:
        self.user: User = None
        self.task_list: list[Task] = []
        self.non_blocked: list[str] = ["127.0.0.1"] # IP addresses that are not blocked
        self.current_task: Task = None

    def set_default_ips(self):
        self.non_blocked = ["127.0.0.1"]

    def set_user(self, user: User) -> None:
        self.user = user

    def get_username(self) -> None:
        return self.user.username

    def get_non_blocked_ips(self) -> None:
        return self.non_blocked

    def set_current_task(self) -> None:
        for i in self.task_list:
            if datetime.now() < i.end_time and datetime.now() > i.start_time:
                self.current_task = i

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
    return render_template("welcome.html")

@app.route('/register')
def placeholder():
    return render_template("register.html")

@app.route('/signin', methods=["GET", "POST"])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        user_password = request.form['password']
        # use util function to sign in
        if login(username, user_password):
            session = Session()
            session.set_user(User(username))
        else:
            pass
        return username, user_password
    return render_template("signin.html")

#access api to check credentials#

user1 = User("fouronf", "Fabrice", "Fouron", "fouronf@wit.edu")

@app.route('/todo/<str:user>')
def todo_list(user):
    # get the tasks to do
    return render_template("todo.html", task_list=[user])

#############################################
if __name__ == '__main__':
    app.run(debug=True)
