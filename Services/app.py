from flask import Flask
from flask import request,jsonify
from demo import register_db,bicycle_db,login_db,transaction_db,gettransaction_db,etlbicycles_db,data_db
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


@app.route('/data',methods = ['get'])
def data():
    res = data_db()
    return jsonify(res)


@app.route('/uploaddata',methods = ['post'])
def uploaddata():
    req = request.files['file'].read()
    
    # Reading the uploaded file content
    #req = request.data['file'] 
    #file_content = req.read()
    import base64

    a = base64.b64encode(req)
    #print(a)
    #print(a.decode())
    #return a

    import io
    import pandas as pd
    import json
    toread = io.BytesIO()
    toread.write(base64.b64decode(a))  # pass your `decrypted` string as the argument here
    toread.seek(0)  # reset the pointer
    df = pd.read_excel(toread)
    test = df.to_json(orient='records')
    input_data = json.loads(test)
    
    response = data_db(input_data)

    #pass direct dataframe
    #how to insert dataframe into sql search like this
    #insert dataframe into database using _tosql function 
    #etl using df no loops directly dump df to sql 

    return response
    


if __name__ == '__main__':
    app.run()



