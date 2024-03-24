from simple_salesforce import Salesforce
import json

sf = Salesforce(username='fouronf@cunning-panda-58x400.com', password='Bibou123', security_token='CPltAZOPCpeY4s3p9AQwA0Tra')

info = {
    "Name": "fabrice",
    "Password__c": "hello"
}

sf.User__c.create(info)
 
desc = sf.User__c.metadata()
# print(desc)
# print(desc)
count = 0
# Below is what you need
for x in sf.describe()["sobjects"]:
    print(x["name"])
    count += 1
print(count)



# field_names = [field['name'] for field in desc['fields']]
# soql = "SELECT {} FROM New_Task__c".format(','.join(field_names))
# results = sf.query_all(soql)
# file = open("newfile.json", "w")

# file.write(json.dumps(results))
# file.close()

describe = open("describe.json", "w")
describe.write(json.dumps(desc))
describe.close()