from flask import Flask, request, send_file
from lib.operations import addition, multiplication, decimal_to_fraction
from lib.constants import TEMPLATE_STRINGS

SERVER_PORT = 8080
STATIC_FOLDER = '../client'
app = Flask(__name__, static_url_path='', static_folder=STATIC_FOLDER)

@app.route('/')
def getIndex():
    return send_file(STATIC_FOLDER + '/index.html')

@app.route('/addition', methods=['POST'])
def postAddition():
    flag=0
    data = request.form
    operands = data['operands']
    numbers = []

    for token in operands.split(','):
        if token=="":
            flag+=1
            continue
        else:
            numbers.append(int(token))
    result = addition(numbers)
    if flag>0 and result==0:
        return TEMPLATE_STRINGS["noop_result"].format(result)
    else:
        return TEMPLATE_STRINGS["op_result"].format(result)

@app.route('/multiplication', methods=['POST'])
def postMultiplication():
    flag=0
    data = request.form
    operands = data['operands']
    numbers = []

    for token in operands.split(','):
        if token=="":
            flag+=1
            continue
        else:
            numbers.append(int(token))
    result = multiplication(numbers)
    if flag>0 and result==0:
        return TEMPLATE_STRINGS["noop_result"].format(result)
    else:
        return TEMPLATE_STRINGS["op_result"].format(result)

@app.route('/decimaltofraction', methods=['POST'])
def postDecimalToFraction():
    data = request.form
    decimal = data['decimal']
    decimal = decimal.replace(' ', '')
    decimal = decimal.replace(',', '.')
    result = decimal_to_fraction(decimal)
    if decimal.count('.') > 1:
        return TEMPLATE_STRINGS['no_decimal']
    else:
        return TEMPLATE_STRINGS['decimal_to_fraction'].format(result)

if __name__ == '__main__':
    app.run(port=SERVER_PORT)
