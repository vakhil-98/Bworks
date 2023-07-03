from flask import Flask
from flask import request,jsonify
from demo import register_db,bicycle_db,login_db,transaction_db
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/',methods = ['get'])
def test():
    return 'hello'

@app.route('/register',methods = ['post'])
def register():
    req = request.get_json()
    print(req)
    res = register_db(req)
    return jsonify(res)


@app.route('/bicycle', methods=['get'])
def bicycle():
    res = bicycle_db()
    return jsonify(res)


@app.route('/login',methods = ['post'])
def login():
    req = request.get_json()
    print(req)
    res = login_db(req)
    return jsonify(res)


@app.route('/transaction',methods = ['post'])
def transaction():
    req = request.get_json()
    print(req)
    res = transaction_db(req)
    return jsonify(res)


@app.route('/gettransaction',methods = ['get'])
def get_transaction():
    res = gettransaction_db()
    return jsonify(res)

@app.route('/etl_bicycles',methods = ['get'])
def etl_bicycles():
    res = etlbicycles_db()
    return jsonify(res)
    
if __name__ == '__main__':
    app.run()

