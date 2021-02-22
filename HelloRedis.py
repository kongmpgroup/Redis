import os
import redis
import json
from flask import Flask ,request,jsonify

app = Flask(__name__)
db=redis.StrictRedis(
    host='node9906-advweb-242.app.ruk-com.cloud'
    ,port=11165
    ,password='CDNtyh07881'
    ,decode_responses=True)


#show key ทั้งหมด
@app.route('/',methods=['GET'])
def Show_keys(): #ทำการสร้างฟัง ก์ชัน Show_keys
    data=db.keys() #สร้าง data มาเก็บข้อมูลจาก db.key 
    data.sort() #เรียงข้อมูล
    req = [] #ประกาศตัวแปล array ชื่อ req 
    for k in data : # สร้างลูป for เอาค่า k มาเก็บ
        req.append(db.hgetall(k)) # db.hgetall แสดงค่าทั้งหมด จาก k แล้วทำการเรียงข้อมูลแบบ list มาเก็บไว้ที่ req
    return jsonify(req) # ทำการสั่งค่ากลับ

# Get Single Staff
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
    app.run()