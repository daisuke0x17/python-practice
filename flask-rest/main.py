# coding: utf-8
from flask import Flask, request, json, jsonify

app = Flask(__name__)
STOCKS = []

@app.route("/stocks", methods=["POST"])
def addStock():
    posted = request.get_json()
    if posted['amount']:
        if isinstance(posted['amount'],int):
            stock = {'name' : posted['name'],
                    'amount': posted['amount'],
                    'sales': 0,
                    }
            STOCKS.append(stock)
        else:
            json = {"message" : "ERROR"}
            return jsonify(json)

    else:
        stock = {'name' : posted['name'],
                 'amount': 1,
                 'sales': 0,
                 }
        STOCKS.append(stock)
    return request.get_data()

@app.route("/stocks", methods=["GET"])
def getStock():
    json = {}
    for item in STOCKS:
        if item['amount'] != 0:
            json[item['name']] = item['amount']
            return jsonify(json)

@app.route("/stocks/<string:name>", methods=["GET"])
def getStockByName(name):
    for item in STOCKS:
        if item['name'] == name:
            json = {
                name: item['amount']
            }
    return jsonify(json)

@app.route("/sales", methods=["POST"])
def saleStock():
    posted = request.get_json()
    if 'price' in posted:
        for item in STOCKS:
            if item['name'] == posted['name']:
                if 'amount' in posted:
                    if item['amount'] < posted['amount']:
                        item['sales'] += item['amount'] * posted['price']
                        item['amount'] = 0
                    else:
                        item['sales'] += posted['amount'] * posted['price']
                        item['amount'] -=  posted['amount']
                else:
                    item['sales'] += posted['price']
                    item['amount'] -= 1
        return request.get_data()
    if 'amount' in posted:
        for item in STOCKS:
            if item['name'] == posted['name']:
                if item['amount'] < posted['amount']:
                    item['amount'] = 0
                else:
                    item['amount'] = item['amount'] - posted['amount']
        return request.get_data()
    else:
        for item in STOCKS:
            if item['name'] == posted['name']:
                if item['amount'] < posted['amount']:
                    item['amount'] = 0
                else:
                    item['amount'] = item['amount'] - 1
        return request.get_data()

@app.route("/sales", methods=["GET"])
def getSales():
    totalSales = 0
    for item in STOCKS:
        if item['sales'] != 0:
            totalSales += item['sales']
    json = {"sales" : totalSales}
    return jsonify(json)

@app.route("/stocks", methods=["DELETE"])
def deleteStock():
    STOCKS.clear()
    return request.get_data()

if __name__ == "__main__":
    app.run()