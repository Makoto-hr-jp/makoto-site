'''
Autor: TM

Svrha: testiranje API-ja

Preduvjeti: - flask server na 127.0.0.1:5000
            - postavljena MySQL baza
'''
# built-in
import requests
import json
from unittest import TestCase,main
makej=lambda d: json.dumps(d)

root="http://127.0.0.1:5000/"

def get_status():
    r=requests.get(url=root+'api-status',json=makej({'a':'b'}))
    print(r.text)
    return r.status_code

def probe_post():
    r=requests.post(url=root+'api-data',json=makej({'a':'b'}))
    return r

class osnovne_funkcije(TestCase):
    def test_status(self):
        self.assertEqual(get_status(),200)

main()
