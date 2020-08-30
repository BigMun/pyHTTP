import requests

#HTTP methods
method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE']

#Carrying out the method tests
for method in method_list:
    req = requests.request(method, 'Enter url here')
    print(method, req.status_code, req.reason)

#Outputting if XST is possible
if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
    print('XST possible')
    #XST = Cross Site Tracing