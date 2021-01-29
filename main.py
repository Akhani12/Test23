from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    with open("j.txt", 'w') as f:
      f.write("harsh")
    return  "hii"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
