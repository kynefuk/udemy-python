import yaml


with open('config.yml', 'w') as config_yml:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, config_yml, default_flow_style=False)
# default_flow_style=Falseを指定しないと、ブロックタイプのymlにならない

with open('config.yml', 'r') as config_yml:
    data = yaml.load(config_yml)
    print(data['web_server']['host'])
