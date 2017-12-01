from flask import Flask, jsonify, request
from handler.supply import SupplyHandler
from handler.transaction import TransactionHandler
from handler.request import RequestHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the Status PR DB Project!'

# ---------- Supply Related -------------

@app.route('/StatusPR/supplier/<int:sid>/resources')
def getSupplierResources(sid):
    return SupplyHandler().searchSupplierResources(sid)

@app.route('/StatusPR/resource/<int:rid>/suppliers')
def getResourceSuppliers(rid):
    return SupplyHandler().searchResourceSupplier(rid)

@app.route('/StatusPR/supply')
def getSupplies():
    if not request.args:
        return SupplyHandler().searchAllsupplies()
    else:
        return SupplyHandler().searchSupplies(request.args) #qty and date



# ------------ Request Related --------------

@app.route('/StatusPR/needer/<int:nid>/resources')
def getNeederResources(nid):
    return RequestHandler().searchNeederResources(nid)

@app.route('/StatusPR/resource/<int:rid>/needer')
def getResourceNeeder(rid):
    return RequestHandler().searchResourceNeeder(rid)

@app.route('/StatusPR/request')
def getRequests():
    if not request.args:
        return RequestHandler().searchAllrequest()
    else:
        return RequestHandler().searchRequests(request.args) #qty and date

# ------------- Transaction Related -------------

@app.route('/StatusPR/transactions')
def getTransactions():
    if not request.args:
        return TransactionHandler().searchAlltransactions()
    else:
        return TransactionHandler().searchTransaction(request.args) #qty and date and price

@app.route('/StatusPR/resource/<int:rid>/needer/supplier')
def getResourceTransactions(rid):
    if not request.args:
        return TransactionHandler().searchAllResourceTransactions(rid)
    else:
        return TransactionHandler().searchResourceTransactions(rid, request.args) #qty and date and price

@app.route('/StatusPR/needer/<int:nid>/resource/supplier')
def getNeederTransactions(nid):
    return TransactionHandler().searchAllNeederTransactions(nid)

@app.route('/StatusPR/supplier/<int:sid>/resource/needer')
def getSupplierTransactions(sid):
    return TransactionHandler().searchAllSupplierTransactions(sid)



if __name__ == '__main__':
    app.run()