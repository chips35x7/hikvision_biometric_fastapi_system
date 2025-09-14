import httpx
from httpx import DigestAuth

"""START TEST FOR CUSTOM FASTAPI ENDPOINT"""

# url = 'http://192.168.1.38/fingerprint-event'
# data = {'test': 'hello'}

# response = httpx.post(url, json=data)

# print(response.status_code)
# print(response.text)

"""END TEST"""

"""START TEST FOR COMMUNICATION BETWEEN CUSTOM ERP API ENDPOINT AND ISAPI"""

from environs import Env

env = Env()
env.read_env()

USERNAME = env.str('USERNAME')
PASSWORD = env.str('PASSWORD')

device_ip = '192.168.1.109'
device_http_port = '80'
server_ip = '192.168.1.38'

# url = f'http://{device_ip}/ISAPI/Event/notification/httpHosts/1'
url = f'http://192.168.1.109:80/ISAPI/Event/notification/httpHosts/1'
auth = DigestAuth(USERNAME, PASSWORD)

with open('subscription.xml') as file:
    xml_data = file.read()

# print(xml_data)
headers = {'Content-Type': 'application/xml'}
response = httpx.put(url, auth=auth, content=xml_data, headers=headers)

print(f'Status: {response.status_code}')
print(f'Response:\n\t{response.text}')

"""END TEST"""