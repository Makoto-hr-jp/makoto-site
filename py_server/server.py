'''
Autor: TM

Svrha: API za razne podatke
'''

def log_msg(tag,text):
    ret="[{}] {}".format(tag,text)
    return ret

# import
try:
    from flask import Flask,Response
except:
    log_msg('FAIL','Could not load flask.')
    quit()
try:
    from flask_restful import Resource,Api,reqparse
except:
    log_msg('FAIL','Could not load flask-restful.')
    quit()
try:
    from postgres import Postgres
except:
    log_msg('FAIL','Could not load postgreSQL module.')
    quit()
'''try:
    #feedback_db=Postgres( ToDo
except:
    log_msg('FAIL','Could not establish link to feedback database.')
'''
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
