import requests

method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE']

for method in method_list:
    req = requests.request(method, 'Enter url here')
    print(method, req.status_code, req.reason)
    #XST = cross site tracing

if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
    print('XST possible')