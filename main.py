import json

with open('/Users/antongrunt/Desktop/project/Hillel_selenium/resources/data.json', 'r') as f:
    secret_variables = json.load(f)
print(secret_variables)
