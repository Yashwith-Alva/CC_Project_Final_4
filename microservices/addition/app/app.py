from flask import Flask
from flask_restful import  Api, Resource

app = Flask(__name__)

@app.route("/<int:number_1>/<int:number_2>", methods=['POST', 'GET'])
def add(number_1,number_2):
    return str(float(number_1)+float(number_2))

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000,
        host="0.0.0.0"
    )