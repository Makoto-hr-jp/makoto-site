'''
Autor: TM

Svrha: upravljanje bazom podataka
'''
#built-in
from hashlib import sha256

# addons
import mysql.connector as sql

# internal
import db_config
from log import log_msg

forbidden=["SELECT","FROM","DELETE","INSERT"]

def connect():
    global dbconn
    log_msg('INFO','Connecting to database...')
    dbconn='OK'
    try:
        ankete_cfg=db_config.get_db_cfg("ankete.cfg")
    except:
        log_msg('FAIL','Missing or broken cfg file "ankete.cfg".')
        dbconn='ERSS'
    try:
        return sql.connect(**ankete_cfg,database='tjedne_ankete')
    except:
        log_msg('FAIL','Could not establish link to feedback database.')

def _check_field(field):
    for f in forbidden:
        if f in field:
            log_msg('WARN',f'Possible SQL injection: "{field}"')
            return False
    return True

def add_entry(link,data):
    ID=sha256(str(data).encode()).hexdigest()
    print(ID)

# database init
ankete=connect()
