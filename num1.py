#-*- coding:utf-8 -*-
from flask import Flask
'''书上在这里的描述是将构造函数的name参数传给Flask程序，Flask用这个参数决定程序的根目录，以便稍后能找到
相对于程序根目录的资源文件. 这句话没有看懂'''

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)