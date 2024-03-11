from flask import Flask, redirect, render_template, request, abort
import socket

app = Flask(__name__)

non_blocked = [] # IP addresses that are not blocked

def get_ip_address(url: str) -> str:
    """ Gets the IP address of a given url """
    ip_address = socket.gethostbyname(url)
    return ip_address

def add_ips(ip: str) -> None:
    """ Adds a given ip address in the non_blocked list """
    non_blocked.append(ip)

@app.before_request
def block_ip():
    client_ip = request.remote_addr
    if client_ip not in non_blocked:
        abort(403)  # Return forbidden status code if IP is blocked


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/placeholder')
def placeholder():
    return "<h1>Placeholder</h1>"

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':
    # app.run(debug=True)
    print(get_ip_address("open.spotify.com"))
