import os
from flask import Flask, request, jsonify, Response, send_from_directory
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
        return("fokof")
    elif request.method == 'GET':
        for argument in request.args:
            if argument == 'search':
                query = request.args.get('search')
                if (request.args.get('limit')): reslimit = request.args.get('limit')
                else: reslimit = 10
                return (jsonify(mpsearch(query, int(reslimit))))

            elif(argument == 'download'):
                file = mpdownload(request.args.get('download'))
                directory = os.curdir
                return send_from_directory(file[2],
                               "hello.txt", as_attachment=True)
                ##return (jsonify({"url":file[1], "title":file[0]+".mp3"}))
