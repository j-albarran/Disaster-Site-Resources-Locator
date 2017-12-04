from flask import Flask, jsonify, request
from handler.supply import SupplyHandler
from handler.transaction import TransactionHandler
from handler.request import RequestHandler
from handler.resources import ResourceHandler
from handler.categories import CategoryHandler
from handler.regions import RegionHandler
from handler.supplier import SupplierHandler
from handler.needer import NeederHandler
from handler.administrator import AdministratorHandler
from handler.account import AccountHandler
from handler.city import CityHandler

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


#   RESOURCEAPP PAGE ROUTE
# =================================================

@app.route('/ResourceApp')
def statusPR():
    return 'RESOURCEAPP PR!'

#   SUPPLIER ROUTES
# =================================================

@app.route('/ResourceApp/supplier')
def getSuppliers():
    # Listing all Suppliers
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    # Searching specific suppliers (pname, plname, city, email, username, region)
    else:
        return SupplierHandler().searchSuppliers(request.args)

#   Looking for a supplier by ID
@app.route('/ResourceApp/supplier/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)

# Looking for suppliers on a specific region
@app.route('/RersourceApp/supplier/city/region/<string:rname>')
def getSuppliersOnRegion(rname):
    return SupplierHandler().getSuppliersOnThisRegion(rname)

#   NEEDER ROUTES
# =================================================

@app.route('/ResourceApp/needer')
def getNeeders():
    # Listing all needers
    if not request.args:
        return NeederHandler().getAllNeeders()
    # Searching specific needers (pname, plname, city, email, username, region)
    else:
        return NeederHandler().searchNeeders(request.args)

# Looking for a needer by ID
@app.route('/ResourceApp/needer/<int:nid>')
def getNeederById(nid):
    return NeederHandler().getNeederById(nid)

# Looking for needers on a specific region
@app.route('/RersourceApp/needer/city/region/<string:rname>')
def getNeedersOnRegion(rname):
    return NeederHandler().getNeedersOnThisRegion(rname)



#   ADMINISTRATOR ROUTES
# =================================================

@app.route('/ResourceApp/administrator')
def getAdministrators():
    # Listing all administrators
    if not request.args:
        return AdministratorHandler().getAllAdministrators()
    # Searching specific administratos (pname, plname, city, email, username, region)
    else:
        return AdministratorHandler().searchAdministrators(request.args)

# Looking for an administrator by ID
@app.route('/ResourceApp/administrator/<int:aid>')
def getAdministratorById(aid):
    return AdministratorHandler().getAdministratorById(aid)

# Looking for administrators on a specific region
@app.route('/RersourceApp/administrator/city/region/<string:rname>')
def getAdministratorsOnRegion(rname):
    return AdministratorHandler().getAdministratorsOnThisRegion(rname)


#   ACCOUNT ROUTES
# =================================================

# Looking for a account by ID
@app.route('/ResourceApp/account/<int:pid>')
def getPersonById(pid):
    return AccountHandler().getAccountByUniqueId(pid)

@app.route('/ResourceApp/account')
def getAllAccounts():
    # Listing all accounts
    if not request.args:
        return AccountHandler().getAllAccounts()
    # Searching specific accounts (pname, plname, city, email, username, region)
    else:
        return AccountHandler().searchAccounts(request.args)

# Looking for accounts on a specific region
@app.route('/RersourceApp/account/city/region/<string:rname>')
def getAccountsOnRegion(rname):
    return AccountHandler().getAccountsOnThisRegion(rname)

#   CITY ROUTES
# =================================================
@app.route('/ResourceApp/city')
def getCities():
    # Listing all cities
    if not request.args:
        return CityHandler().getAllCities()
    # Searching for cities on a specific region
    else:
        return CityHandler().searchCities(request.args)

# Looking or a specific city by name
@app.route('/ResourceApp/city/<string:cname>')
def getCityByName(cname):
    return CityHandler().getCitiesByName(cname)

if __name__ == '__main__':
    app.run()