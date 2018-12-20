'''
Autor: TM

Svrha: API za razne podatke
'''
# built-in
from datetime import datetime

def log_msg(tag,text):
    ret=f"{str(datetime.now()):<28} [{tag}] {text}"
    print(ret)
    return ret

def fail_gracefully():
    try:
        feedback_db.close()
    except:
        pass
    quit()

log_msg('INFO','Starting REST server...')

# addons / internal
try:
    from flask import Flask,Response
except:
    log_msg('FAIL','Could not load flask.')
    fail_gracefully()
try:
    from flask_restful import Resource,Api,reqparse
except:
    log_msg('FAIL','Could not load flask-restful.')
    fail_gracefully()
db_ok=True
try:
    import mysql.connector as sql
except:
    log_msg('FAIL','Could not load mysql connector module.')
    db_ok=False
try:
    import db_config
except:
    log_msg('FAIL','Could not load database configuration module.')
    db_ok=False
try:
    ankete_cfg=db_config.get_db_cfg("ankete.cfg")
except:
    log_msg('FAIL','Missing or broken cfg file "ankete.cfg".')
    db_ok=False
try:
    feedback_db=sql.connect(**ankete_cfg,database='tjedne_ankete')
except:
    log_msg('FAIL','Could not establish link to feedback database.')

# builtin
import json

app=Flask(__name__)
api=Api(app)

@app.route("/api-status",methods=['GET'])
def get_status():
    ''' dostupnost raznih serverskih resursa
            status: OK - sve radi
                    WARN - čudno, ali ne kritično
                    ERRS - nešto ne radi
    '''
    return Response(json.dumps({'status':'OK'}))

app.run(debug=True)
