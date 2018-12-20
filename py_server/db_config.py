'''
Autor: TM

Svrha: Upravljanje konfiguracijom za mysql
'''
import json

def make_db_cfg(file):
    cfg={'user':input("user: "),
         'password':input("pass: "),
         'host':input("host: ")}
    with open(file,"w") as f:
        f.write(json.dumps(cfg))

def get_db_cfg(file):
    with open(file,"r") as f:
        ret=json.loads(f.read())
    return ret
