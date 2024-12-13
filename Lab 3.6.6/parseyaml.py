import json
import yaml

# Відкриття YAML файлу
with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

# Друк YAML даних
print(ouryaml)

# Друк значень маркера та інформації про термін дії
print("The access token is: {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))

# Друк JSON формату
print("\n\n---")
print(json.dumps(ouryaml, indent=4))
