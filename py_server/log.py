'''
Autor: TM

Svrha: dragi dnevniče
'''
# built-in
from datetime import datetime

def log_msg(tag,text):
    ret=f"{str(datetime.now()):<28} [{tag}] {text}"
    print(ret)
    return ret
