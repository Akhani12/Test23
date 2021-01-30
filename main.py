from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    def writeToFile(path, content):
       file = open(path, "w")
       file.write(content)
       file.close()
  
  
    PATH_TO_MY_FILE = './example.txt'
    CONTENT_FOR_MY_FILE = 'Example\nThis is on line 2 of a text file.\n\nThe end.'

    writeToFile(PATH_TO_MY_FILE, CONTENT_FOR_MY_FILE)
    return  "hii"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
