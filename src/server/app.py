from flask import Flask, request, send_file
from lib.operations import addition
from lib.constants import TEMPLATE_STRINGS

SERVER_PORT = 8080
STATIC_FOLDER = '../client'
app = Flask(__name__, static_url_path='', static_folder=STATIC_FOLDER)

@app.route('/')
def getIndex():
    return send_file(STATIC_FOLDER + '/index.html')

@app.route('/addition', methods=['POST'])
def postAddition():
    data = request.form
    operands = data['operands']
    numbers = []
    
    for token in operands.split(','):
        numbers.append(int(token))
    
    result = addition(numbers)

    return TEMPLATE_STRINGS["op_result"].format(result)

if __name__ == '__main__':
    app.run(port=SERVER_PORT)
