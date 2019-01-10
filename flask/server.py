from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index.html')
def content():
    text = open('flask/index.html')
    content = text.read()
    text.close()
    return content

if __name__ == '__main__':
    app.run(debug=True, port=2001, host='0.0.0.0')
