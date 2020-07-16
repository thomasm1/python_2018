from flask import Flask, jsonify, request, redirect
app = Flask(__name__)

currencies = [{'id': 1, 'name': 'LiteCoin', 'symbol':'LTC'}, {'id': 2, 'name': 'Bitcoin', 'symbol':'BTC'}, {'id': 3, 'name': 'Ethereum', 'symbol':'ETH'}]

@app.route('/currency', methods=['GET'])
def returnAll():
    return jsonify({'currencies': currencies})

@app.route('/currency/<string:name>', methods=['GET'])
def returnOne(name):
    currs = [currency for currency in currencies if currency['name'] == name]
    return jsonify({'currency': currs[0]})

@app.route('/currency', methods=['POST'])
def addOne():
    currency = {'name': request.json['name']}
    currencies.append(currency)
    return jsonify({'currencies': currencies})

@app.route('/currency/<string:name>', methods=['PUT'])
def editOne(name):
    currs = [currency for currency in currencies if currency['name'] == name] 
    currs[0]['name'] = request.json['name']
    return jsonify({'currency': currs[0]}) 

@app.route('/currency/<string:name>', methods=['DELETE'])
def removeOne(name):
    curr = [currency for currency in currencies if currency['name'] == name] 
    currencies.remove(curr[0])
    return jsonify({'currencies': currencies}) 

@app.route('/')
def re_direct():
    return redirect("/currency") 

if __name__ == '__main__':
    app.run(debug=True, port=5010)