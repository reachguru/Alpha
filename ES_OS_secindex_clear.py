import requests
from requests.auth import HTTPBasicAuth

# Define connection parameters
ip = '10.129.5.93'
admin_user = 'admin'
admin_password = 'j!rXUC9fyiRx'
port = '9200'
base_url = f'http://{ip}:{port}/'
# Construct the URL for getting indices
get_indices_request = f'{base_url}_cat/indices/security-auditlog*?h=index'
# Make the GET request to retrieve indices
response = requests.get(get_indices_request, auth=HTTPBasicAuth(admin_user, admin_password))
# Check if the GET request was successful
if response.ok:
    # Split the response text into lines and iterate over each line
    for index in response.text.splitlines():
        # Construct the URL for the DELETE request
        delete_url = f'{base_url}{index}'

        # Make the DELETE request to delete the index
        delete_response = requests.delete(delete_url, auth=HTTPBasicAuth(admin_user, admin_password))

        # Print the result of the DELETE request
        print(f'Deleting index {index}: {delete_response.text}')
else:
    print(f'Error retrieving indices: {response.status_code} {response.text}')