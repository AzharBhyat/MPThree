import os
from flask import Flask, request, jsonify, Response, send_from_directory, redirect
from flask_cors import CORS
from mpthree import mpsearch, mpdownload

app = Flask(__name__)
CORS(app)

def search(query):
    results = mpsearch(query)
    results = list(results)
    titles = []
    for i in range(len(results)):
        titles.append(results[i]["title"])
    return (titles)


@app.route('/mpthree', methods=['GET','POST'])
def mpthree():
    if request.method == 'POST':
    #check user details from db
        return("Oops thats a no no..")
    elif request.method == 'GET':
        for argument in request.args:
            if argument == 'search':
                query = request.args.get('search')
                if (request.args.get('limit')): reslimit = request.args.get('limit')
                else: reslimit = 10
                return (jsonify(mpsearch(query, int(reslimit))))

            elif(argument == 'download'):
                dl = mpdownload(request.args.get('download'))
                file = dl[0]
                file = BytesIO(file)
                return (send_file(file, download_name=dl[1]+'.mp3', as_attachment=True))
