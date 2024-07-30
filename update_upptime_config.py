import os
import yaml

dns_records_dir = './phac-dns/dns-records'
upptime_config_path = './.upptime.yml'

def get_domains_from_yaml(directory):
    domains = []
    for filename in os.listdir(directory):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(directory, filename), 'r') as file:
                content = yaml.safe_load(file)
                if 'spec' in content and 'name' in content['spec']:
                    domain = content['spec']['name']
                    domains.append(domain.rstrip('.'))
    return domains

def update_upptime_config(domains, config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    config['sites'] = [{'name': domain, 'url': domain} for domain in domains]

    with open(config_path, 'w') as file:
        yaml.safe_dump(config, file)

if __name__ == '__main__':
    domains = get_domains_from_yaml(dns_records_dir)
    update_upptime_config(domains, upptime_config_path)
