from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # name = request.args['name']
    # ids = request.args['ids']
    # return "<h1>My Name Is "+name+" And id is "+str(ids)+"</h1>"
    return  "hii"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
