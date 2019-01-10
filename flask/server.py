from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

counter_file = open('flask/counter.txt', 'r')
actual_counter = int(counter_file.read(1))
counter_file.close()

@app.route('/index.html')
def content():
    global actual_counter
    actual_counter += 1
    counter_file = open('flask/counter.txt', 'w')
    counter_file.write(str(actual_counter))
    counter_file.close()
    text = open('flask/index.html')
    content = text.read()
    text.close()
    return content


@app.route('/count')
def visitors():
    return str(actual_counter)

if __name__ == '__main__':
    app.run(debug=True, port=2001, host='0.0.0.0')
