from flask import Flask,jsonify,request
from data import data
app=Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        'data':data,
        'message':'success'
    }),200

@app.route('/star')
def stars():
    name=request.args.get('Name')
    all_stars=next(item for item in data if item['Name']==name)
    return jsonify({
        'data':all_stars,
        'message':'success'
    }),200
if __name__=='__main__':
    app.run()
#ngrok http 5000