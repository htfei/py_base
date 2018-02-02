'''
aaa
'''
import json
import requests

RSP = requests.get('http://httpbin.org/stream/20', stream=True)

for line in RSP.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print json.loads(decoded_line)
