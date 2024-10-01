import yaml

# Path to the settings.yml file
settings_file = '/usr/local/searxng/searx/settings.yml'

# Load the existing YAML configuration
with open(settings_file, 'r') as file:
    config = yaml.safe_load(file)

# Ensure the 'formats' key exists and add 'json' if it is not present
if 'formats' in config['search'] and 'json' not in config['search']['formats']:
    config['search']['formats'].append('json')

# Write the updated configuration back to the file
with open(settings_file, 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

print("JSON format added successfully.")
