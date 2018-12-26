'''
Autor: TM

Svrha: upravljanje bazom podataka
'''
#built-in
from hashlib import sha256
from datetime import datetime

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

req_keys=set(('gradivo','listic','zadaca','komentar'))
def add_entry(link,data):
    if type(data)!=dict: return False
    if set(data.keys())!=req_keys: return False
    str_repr=(f"{data['gradivo']}"
              f"{data['listic']}"
              f"{data['zadaca']}"
              f"{data['komentar']}")
    ID=sha256(str_repr.encode()).hexdigest()
    date=datetime.now().strftime("%Y-%m-%d")
    query=("INSERT INTO odgovori "
           "(ID, datum, gradivo, listic, zadaca, komentar) "
           f"""VALUES ("{ID}", "{date}", {data['gradivo']}, """
           f"""{data['listic']}, {data['zadaca']}, "{data['komentar']}")""")
    print(query)
    cursor=link.cursor()
    cursor.execute(query)
    link.commit()
    cursor.close()
    return True

# database init
ankete=connect()
