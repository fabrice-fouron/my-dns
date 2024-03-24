import socket
from simple_salesforce import Salesforce
import json



def get_ip(url: str) -> str :
    return socket.gethostbyname(url)

def register(username: str, password: str) -> None:
    sf = Salesforce(username='fouronf@cunning-panda-58x400.com', password='Bibou123', security_token='CPltAZOPCpeY4s3p9AQwA0Tra')
    info = {
        "Name": username,
        "Password__c": password
    }
    sf.User__c.create(info)
    pass


def login(username: str, password: str) -> None:
    sf = Salesforce(username='fouronf@cunning-panda-58x400.com', password='Bibou123', security_token='CPltAZOPCpeY4s3p9AQwA0Tra')
    info = {
        "Name": username,
        "Password__c": password
    }
    # check against the api if the credentials entered match

    
    pass
