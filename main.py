from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "Perfect hai Boss"
    
if __name__ == '__main__':
    app.run()
