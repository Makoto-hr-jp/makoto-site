'''
Autor: TM

Svrha: API za razne podatke
'''

# import
from flask import Flask,Response
from flask_restful import Resource,Api,reqparse

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
