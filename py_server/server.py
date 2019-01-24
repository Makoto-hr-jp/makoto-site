'''
Autor: TM

Svrha: API za razne podatke
'''
# built-in
import json

def fail_gracefully():
    try:
        feedback_db.close()
    except:
        pass
    quit()

# addons
from flask import Flask,Response,request,send_from_directory
from flask_restful import Resource,Api,reqparse

# internal
import db_ctrl
from log import log_msg
log_msg('INFO','Starting REST server...')

# app init
app=Flask(__name__)
api=Api(app)

@app.route("/",methods=['GET'])
def serve_index():
    return send_from_directory('../ng_frontend','index.html')

@app.route("/<path:path>",methods=['GET'])
def serve_path(path):
    return send_from_directory('../ng_frontend',path)

@app.route("/api-status",methods=['GET'])
def get_status():
    ''' dostupnost raznih serverskih resursa
            status: OK - sve radi
                    WARN - čudno, ali ne kritično
                    ERRS - nešto ne radi
    '''
    st='OK'
    components=[db_ctrl.dbconn]
    for c in components:
        if st=='OK':
            if c!='OK': st=c
        elif st=='WARN':
            if c!='OK':
                st=c
    status={'status':st,
            'dbconn':db_ctrl.dbconn}
    if request.json: print("data:",request.json)
    return Response(json.dumps(status))

@app.route("/api-data",methods=['POST'])
def post_data():
    print("I got some stuff!")
    return "OK"

app.run(debug=True)
