import httpx
import json

from httpx import DigestAuth
from environs import Env

env = Env()
env.read_env()

USERNAME = 'admin'
PASSWORD = env.str('PASSWORD')

"""START DEVICE COMMUNICATION TEST OVER ISAPI"""

# isapi_endpoint = 'http://192.168.1.100:800/ISAPI/AccessControl/UserInfo/Search?format=json'
# isapi_endpoint = 'http://192.168.1.100:800/ISAPI/AccessControl/UserInfo/Record'
# device_info = 'http://192.168.1.109/ISAPI/System/deviceInfo'
# isapi_endpoint = 'http://192.168.1.109/ISAPI/System/deviceInfo'

# auth = httpx.DigestAuth('admin', password)
# headers = {'Accept': 'application/json'}

# with httpx.Client(auth=auth) as client:
#     response = client.get(device_info)
#     print(f'Status Code: {response.status_code}')
#     print(f'Response:\n\t{response.text}') 

"""END TEST"""

"""START COMMUNICATION TEST WITH CUSTOM PHP BASED API"""

# test_url = 'http://localhost:8000/log_system.php'

# def send_data(file_path:str ,url:str):
#     with open(file_path) as file:
#         employee_logs = json.load(file)

#         for employee_log in employee_logs:
#             # print(employee_log)
#             response = httpx.post(url, data=employee_log)
#             print(f'Sent {employee_log.get('employee_id')}\nStatus: {response.json()['status']}, {response.json()['message']}')

# send_data('data.json', test_url)

"""END TEST"""

device_ip = '192.168.1.109'
device_http_port = '80'

url = f'http://{device_http_port}:{device_http_port}/ISAPI/Event/notification/httpHosts/1'
auth = DigestAuth(USERNAME, PASSWORD)

with open('subscription.xml', 'r') as file:
    xml_data = file.read()

headers = {'Content Type': 'application/xml'}

with httpx.Client(auth=auth) as client:
    response = client.put(url, data=xml_data, headers=headers)
    print(f'Status Code: {response.status_code}')
    print(f'Response: \n\t{response.text}')