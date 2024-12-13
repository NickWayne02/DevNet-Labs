import json
import yaml

# Відкриття JSON файлу
with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

# Друк JSON даних
print(ourjson)

# Друк значень маркера та інформації про термін дії
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

# Друк YAML формату
print("\n\n---")
print(yaml.dump(ourjson))
