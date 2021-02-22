import os
import redis
import json
from flask import Flask ,request,jsonify

app = Flask(__name__)
db=redis.StrictRedis(
    host='10.100.3.39'
    ,port=6379
    ,password='CDNtyh07881'
    ,decode_responses=True)


#show all key
@app.route('/',methods=['GET'])
def Show_keys():
    data=db.keys()  
    data.sort()
    req = []
    for k in data :
        req.append(db.hgetall(k))
    return jsonify(req) 

# Get Single book
@app.route('/<Key>', methods=['GET'])
def get_Book(Key):
    Book = db.hgetall(Key)
    return jsonify(Book)

# Update a Staff*****
@app.route('/insert/<Key>', methods=['PUT'])
def update_Book(Key):
    
    id = request.json['id']
    price = request.json['price']
    username = request.json['username']
    
    
    updatedata = {"username":username, "price":price, "id":id}     
    db.hmset(Key,updatedata)   

    return jsonify(updatedata)

# insert a Staff*****
@app.route('/insert', methods=['POST'])
def insert_Book():
    
    id = request.json['id']
    price = request.json['price']
    username = request.json['username']
    key = request.json['key']

    insertdata = {"username":username, "price":price, "id":id}     
    db.hmset(key,insertdata)   

    return jsonify(insertdata)

# Delete Staff*****
@app.route('/delete/<Key>', methods=['DELETE'])
def get_delete(Key):
    deleteBook = db.delete(Key)
    return jsonify(deleteBook)


@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000) 