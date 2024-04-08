import socket
from simple_salesforce import Salesforce
import json
from Task import Task


credentials = {
    'username': 'fouronf@cunning-panda-58x400.com',
    'password': 'Bibou123',
    'token': 'CPltAZOPCpeY4s3p9AQwA0Tra'
}


sf = Salesforce(username=credentials['username'], password=credentials['password'], security_token=credentials['token'])


def get_ip(url: str) -> str :
    """This function returns the IP address that maps to a given URL"""
    return socket.gethostbyname(url)


def register(username: str, password: str) -> None:
   
    if not already_exists(username):  # if the user already exists, avoid creating another account
        pass
    else:
        info = {
            "Name": username,
            "Password__c": password
        }
        sf.New_User__c.create(info) # create a new user login and send to Salesforce

    # open the todo list page

def login(username: str, password: str) -> bool:
    info = {
        "Name": username,
        "Password__c": password
    }
    # check against the api if the credentials entered match
    if already_exists(username):
        if get_password(username) == password:
            # password matches - login successful
            # return True to open todo list page
            return True
        return False
    else:
        # password doesn't match or account doesn't exist
        return False


def already_exists(username):
    if get_info(username)['totalSize'] > 0:
        return True
    return False


def get_info(username):  
    field_names = ['Id', 'Name', 'Password__c']
    soql = "SELECT {} FROM New_User__c WHERE Name = '".format(','.join(field_names))
    soql += username + "'"
    results = sf.query(soql)
    return results

def get_user_id(username):
    results = get_info(username)

    json_result = []
    for record in results['records']:
        json_result.append({
            'Id': record['Id'],
            'Name': record['Name'],
            'Password': record['Password__c']
        })
    return json_result[0]['Id']

def get_password(username):
    results = get_info(username)

    json_result = []
    for record in results['records']:
        json_result.append({
            'Name': record['Name'],
            'Password': record['Password__c']
        })
    return json_result[0]['Password']


def get_todo_list(username):
    ''' retrieves the todo list from Salesforce
        loops through each task in the databse and finds each one
        matches the user in question '''
    field_names = ['Name', 'New_User__c', 'Tool__c']
    soql = "SELECT {} FROM New_Task__c".format(','.join(field_names))
    
    results = sf.query(soql)
    json_result = []
    for record in results['records']:
        json_result.append({
            'Name': record['Name'],
            'New_User__c': record['New_User__c'],
            'Tool__c': record['Tool__c']
        })

    todo_list: Task = [] # list of tasks

    for i in json_result:
        if i['New_User__c'] == get_user_id(username):
            new_task = Task(i['Name'])
            new_task.set
            todo_list.append(new_task)
    
    for i in todo_list:
        print(i)

def main():
    contact = sf.New_User__c.get('a0BHp000015S93bMAC')
    print(get_todo_list('fabricefouron'))

main()
