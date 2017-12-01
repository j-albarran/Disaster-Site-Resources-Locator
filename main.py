from flask import Flask, jsonify, request
from handler.supply import SupplyHandler
from handler.transaction import TransactionHandler
from handler.request import RequestHandler
from handler.resources import ResourceHandler
from handler.categories import CategoryHandler
from handler.regions import RegionHandler

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello, this is the Disaster-Site-Resources-Locator project.'

# Resource routes

@app.route('/ResourceApp/resources')
def getAllResources():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResources(request.args) # RName, RQty and RCategory

@app.route('/ResourceApp/resource/<int:id>')
def getResourceById(id):
    return ResourceHandler().getResourceById(id)

# Category routes

@app.route('/ResourceApp/categories')
def getAllCategories():
    return CategoryHandler().getAllCategories()

@app.route('/ResourceApp/category/<string:name>')
def getCategoryByName(name):
    return CategoryHandler().getCategoryByName(name)

# Region routes

@app.route('/ResourceApp/regions')
def getAllRegions():
    return RegionHandler().getAllRegions()

@app.route('/ResourceApp/region/<string:name>')
def getRegionByName(name):
    return RegionHandler().getRegionByName(name)


# ---------- Supply Related -------------

@app.route('/ResourceApp/supplier/<int:sid>/resources')
def getSupplierResources(sid):
    return SupplyHandler().searchSupplierResources(sid)

@app.route('/ResourceApp/resource/<int:rid>/suppliers')
def getResourceSuppliers(rid):
    return SupplyHandler().searchResourceSupplier(rid)

@app.route('/ResourceApp/supply')
def getSupplies():
    if not request.args:
        return SupplyHandler().searchAllsupplies()
    else:
        return SupplyHandler().searchSupplies(request.args) #qty and date



# ------------ Request Related --------------

@app.route('/ResourceApp/needer/<int:nid>/resources')
def getNeederResources(nid):
    return RequestHandler().searchNeederResources(nid)

@app.route('/ResourceApp/resource/<int:rid>/needer')
def getResourceNeeder(rid):
    return RequestHandler().searchResourceNeeder(rid)

@app.route('/ResourceApp/request')
def getRequests():
    if not request.args:
        return RequestHandler().searchAllrequest()
    else:
        return RequestHandler().searchRequests(request.args) #qty and date

# ------------- Transaction Related -------------

@app.route('/ResourceApp/transactions')
def getTransactions():
    if not request.args:
        return TransactionHandler().searchAlltransactions()
    else:
        return TransactionHandler().searchTransaction(request.args) #qty and date and price

@app.route('/ResourceApp/resource/<int:rid>/needer/supplier')
def getResourceTransactions(rid):
    if not request.args:
        return TransactionHandler().searchAllResourceTransactions(rid)
    else:
        return TransactionHandler().searchResourceTransactions(rid, request.args) #qty and date and price

@app.route('/ResourceApp/needer/<int:nid>/resource/supplier')
def getNeederTransactions(nid):
    return TransactionHandler().searchAllNeederTransactions(nid)

@app.route('/ResourceApp/supplier/<int:sid>/resource/needer')
def getSupplierTransactions(sid):
    return TransactionHandler().searchAllSupplierTransactions(sid)

if __name__ == '__main__':
    app.run()